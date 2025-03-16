from django.db import models
from django.utils import timezone
from queues.models import Window, Status, Service, Category
from queues.seeds import constants


def get_default_status():
    return Status.objects.get(name="waiting").id

def default_numbering(queue):
    queue_no = 1
    if queue.service.name == "Inquire":
        last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__date=timezone.localtime(timezone.now()).date(),
            service=queue.service,
        ).last()
        if last_queue is not None:
            queue_no = last_queue.queue_no + 1
        return (queue_no, f"Q{queue_no}")

    last_queue = Queue.objects.filter(
        branch=queue.branch,
        created_at__date=timezone.localtime(timezone.now()).date(),
        category=queue.category,
    ).exclude(service=Service.objects.get(name="Inquire", branch=queue.branch)).last()
    if last_queue is not None:
        queue_no = last_queue.queue_no + 1
    category_initial = queue.category.name[0].upper()
    return (queue_no, f"{category_initial}{queue_no}")
    
def get_queue_no_and_code(queue):
    return default_numbering(queue)
   
class Queue(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)      # required
    category = models.ForeignKey("Category", on_delete=models.CASCADE)  # required
    service = models.ForeignKey("Service", on_delete=models.CASCADE)    # required
    service_type = models.CharField(max_length=50, blank=True, null=True)
    window = models.ForeignKey("Window", on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey("Status", default=get_default_status, on_delete=models.CASCADE)
    queue_code = models.CharField(max_length=10, blank=True, null=True)
    applicant_name = models.CharField(max_length=50)                    # required
    no_applicant = models.PositiveIntegerField()                        # required
    applicant_type = models.CharField(max_length=50, blank=True, null=True)
    is_senior_pwd = models.BooleanField(default=False)
    queue_no =  models.PositiveIntegerField(blank=True, null=True)
    coordinator_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    called_at = models.DateTimeField(blank=True, null=True)
    is_called = models.BooleanField(default=False)    
    is_priority = models.BooleanField(default=False)    
    applicant_photo = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.service} - {self.no_applicant} - {self.applicant_name} - {self.queue_code} - {self.status}"
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.is_called:
            self.status = Status.objects.get(name="now-serving")
            self.called_at = timezone.now()
        if self.queue_no is None:
            self.queue_no, self.queue_code = get_queue_no_and_code(self)
        if self.status == Status.objects.get(name="complete") or self.status == Status.objects.get(name="pending") or self.status == Status.objects.get(name="return"):
            self.applicant_photo = None
            
        super(Queue, self).save(*args, **kwargs)
    
    def get_current_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            created_at__date=timezone.localtime(timezone.now()).date()
        )
    
    def get_current_waiting_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__date=timezone.localtime(timezone.now()).date()
        )
    
    def get_current_now_serving_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="now-serving").id,
            created_at__date=timezone.localtime(timezone.now()).date()
        )
    
# ---------------------- RECEIVER ---------------------- #
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@receiver([post_save, post_delete], sender=Queue)
def ws_notify_now_serving_queues(sender, instance, **kwargs):
    branch = instance.branch
    
    group_name = f"now-serving-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "now-serving"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)

@receiver([post_save, post_delete], sender=Queue)
def ws_notify_waiting_queues(sender, instance, **kwargs):
    branch = instance.branch
    
    group_name = f"waiting-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "waiting"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)
    
@receiver([post_save, post_delete], sender=Queue)
def ws_notify_current_stats(sender, instance, **kwargs):
    branch = instance.branch
    
    group_name = f"stats-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "stats"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)

@receiver([post_save, post_delete], sender=Queue)
def ws_notify_controller_queues(sender, instance, **kwargs):
    branch = instance.branch
    
    group_name = f"controller-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "controller"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)

@receiver([post_save], sender=Queue)
def ws_notify_called_queue(sender, instance, **kwargs):
    branch = instance.branch
    applicant_name = instance.applicant_name
    queue_code = instance.queue_code
    applicant_photo = instance.applicant_photo
    
    if instance.is_called:
        window = Window.objects.get(id=instance.window_id)
        
        group_name = f"call-queue-{branch.id}"
        event = {
            "type": "queue.call",
            "name": applicant_name,
            "window_name": window.name,
            "queue_code": queue_code,
            "applicant_photo": applicant_photo
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
        
        instance.is_called = False
        instance.save()
    
# @receiver([post_save, post_delete], sender=Queue)
# def ws_notify_current_tourism_total(sender, instance, **kwargs):
#     branch = instance.branch
    
#     channel_layer = get_channel_layer()
#     group_name = f"current-tourism-stat-queue-{branch.id}"
#     event = {
#         "type": "queues.update",
#         "queue_status": "current-tourism-stat"
#     }
#     async_to_sync(channel_layer.group_send)(group_name, event)