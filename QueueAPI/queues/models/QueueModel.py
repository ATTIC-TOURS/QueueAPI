from django.db import models
from django.utils import timezone
from queues.models import Status, Service, Category


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
        service__category=queue.service.category,
    ).last()
    if last_queue is not None:
        queue_no = last_queue.queue_no + 1
    category_initial = queue.service.category.name[0].upper()
    return (queue_no, f"{category_initial}{queue_no}")
    
def get_queue_no_and_code(queue):
    return default_numbering(queue)
   
class Queue(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)      # required #OK
    service = models.ForeignKey("Service", on_delete=models.CASCADE)    # required #OK
    service_type = models.CharField(max_length=50, blank=True, null=True) #OK
    called_by = models.CharField(max_length=50, blank=True, null=True) #OK
    status = models.ForeignKey("Status", default=get_default_status, on_delete=models.CASCADE) #OK
    queue_code = models.CharField(max_length=10, blank=True, null=True) #OK
    applicant_name = models.CharField(max_length=50)                    # required #OK
    no_applicant = models.PositiveIntegerField()                        # required #OK
    applicant_type = models.CharField(max_length=50, blank=True, null=True) #OK
    is_senior_pwd = models.BooleanField(default=False)                          #OK
    queue_no =  models.PositiveIntegerField(blank=True, null=True)              #OK
    coordinator_name = models.CharField(max_length=100, blank=True, null=True)  #OK
    created_at = models.DateTimeField(default=timezone.now)                     #OK
    updated_at = models.DateTimeField(blank=True, null=True)                    #OK
    called_at = models.DateTimeField(blank=True, null=True)                     #OK
    is_priority = models.BooleanField(default=False)                            #OK
    applicant_photo = models.TextField(blank=True, null=True)                   #OK
    controller_id = models.CharField(max_length=100, blank=True, null=True)         #OK
    
    def __str__(self):
        return f"{self.service} - {self.no_applicant} - {self.applicant_name} - {self.queue_code} - {self.status}"
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.controller_id:
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

@receiver([post_save], sender=Queue)
def ws_notify_updated_queue(sender, instance, **kwargs):
    from queues.serializers import QueueSerializer
    branch = instance.branch
    queueSerializer = QueueSerializer(instance)
    group_name = f"queue_update_branch_{branch.id}"
    event = {
        "type": "queue.update.message", 
        "message": queueSerializer.data
    }
    async_to_sync(channel_layer.group_send)(group_name, event)

@receiver([post_delete], sender=Queue)
def ws_notify_removed_queue(sender, instance, **kwargs):
    from queues.serializers import QueueSerializer
    branch = instance.branch
    queueSerializer = QueueSerializer(instance)
    group_name = f"queue_remove_branch_{branch.id}"
    event = {
        "type": "queue.remove.message", 
        "message": queueSerializer.data
    }
    async_to_sync(channel_layer.group_send)(group_name, event)
    
@receiver([post_save, post_delete], sender=Queue)
def ws_notify_current_stats(sender, instance, **kwargs):
    branch = instance.branch
    
    group_name = f"stats-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "queue_status": "stats"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)