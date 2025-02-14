from django.db import models
from django.utils import timezone
from queues.models import Window, Status
from queues.apiviews.utils.time import get_starting_of_current_manila_timezone
from queues.seeds import constants


def get_default_status():
    return Status.objects.get(name="waiting").id

def other_branch_numbering_and_code(queue):
    queue_no = 1
    last_queue = Queue.objects.filter(
        branch=queue.branch,
        created_at__gte=get_starting_of_current_manila_timezone(),
        category=queue.category,
    ).last()
    if last_queue is not None:
        queue_no = last_queue.queue_no + 1
    category_initial = queue.category.name[0].upper()
    service_initial = queue.service.name[0].upper()
    return (queue_no, f"{category_initial}-{service_initial}{queue_no}")

def main_branch_numbering_and_code(queue):
    queue_no = 1
    if queue.applicant_type == "PTAA":
        ptaa_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            applicant_type="PTAA"
        ).last()
        if ptaa_last_queue is not None:
            queue_no = ptaa_last_queue.queue_no + 1
        return (queue_no, f"PTAA-{queue_no}")
    
    elif queue.applicant_type == "MAN POWER":
        manpower_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            applicant_type="MAN POWER"
        ).last()
        if manpower_last_queue is not None:
            queue_no = manpower_last_queue.queue_no + 1
        return (queue_no, f"M-{queue_no}")
    
    elif queue.service_type == "INQUIRE":
        inquire_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            service_type="INQUIRE"
        ).last()
        if inquire_last_queue is not  None:
            queue_no = inquire_last_queue.queue_no + 1
        return (queue_no, f"I-{queue_no}")
    
    elif queue.service_type == "ADDITIONAL DOCUMENTS":
        addocs_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            service_type="ADDITIONAL DOCUMENTS"
        ).last()
        if addocs_last_queue is not None:
            queue_no = addocs_last_queue.queue_no + 1
        return (queue_no, f"A-{queue_no}")
    
    elif queue.service_type == "PENDING DOCUMENTS":
        pending_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            service_type="PENDING DOCUMENTS"
        ).last()
        if pending_last_queue is not None:
            queue_no = pending_last_queue.queue_no + 1
        return (queue_no, f"P-{queue_no}")
    
    elif queue.applicant_type == "WALK-IN":
        walkin_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            applicant_type="WALK-IN"
        ).last()
        service_initial = queue.service.name[0].upper()
        if walkin_last_queue is not None:
            queue_no = walkin_last_queue.queue_no + 1
        return (queue_no, f"J-{service_initial}{queue_no}")
    
    elif queue.applicant_type == "TRAVEL AGENCY":
        ta_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            applicant_type="TRAVEL AGENCY"
        ).last()
        service_initial = queue.service.name[0].upper()
        if ta_last_queue is not None:
            queue_no = ta_last_queue.queue_no + 1
        return (queue_no, f"TA-J-{service_initial}{queue_no}")
    
    elif queue.category_id == constants.TICKET_MAIN_OFFICE_ID:
        ticket_last_queue = Queue.objects.filter(
            branch=queue.branch,
            created_at__gte=get_starting_of_current_manila_timezone(),
            category_id=constants.TICKET_MAIN_OFFICE_ID
        ).last()
        if ticket_last_queue is not None:
            queue_no = ticket_last_queue.queue_no + 1
        return (queue_no, f"T-{queue_no}")
    
    else:
        return other_branch_numbering_and_code(queue)
    
def get_queue_no_and_code(queue):
    if queue.branch_id == constants.MAIN_OFFICE_ID:
        return main_branch_numbering_and_code(queue)
    else:
        return other_branch_numbering_and_code(queue)

class Queue(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=False, null=False)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, blank=False, null=False)
    service_type = models.CharField(max_length=50, blank=True, null=True)
    window = models.ForeignKey("Window", on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey("Status", default=get_default_status, on_delete=models.CASCADE, blank=False, null=False)
    queue_code = models.CharField(max_length=10, blank=True, null=True)
    applicant_name = models.CharField(max_length=50, blank=False, null=False)
    no_applicant = models.PositiveIntegerField(blank=True, null=True)
    applicant_type = models.CharField(max_length=50, blank=True, null=True)
    is_senior_pwd = models.BooleanField(default=False)
    queue_no =  models.PositiveIntegerField(blank=True, null=True)
    coordinator_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    called_at = models.DateTimeField(blank=True, null=True)
    is_called = models.BooleanField(default=False, blank=False, null=False)    
    is_priority = models.BooleanField(default=False, blank=False, null=False)    
    
    def __str__(self):
        return f"{self.service} - {self.no_applicant} - {self.applicant_name} - {self.queue_code} - {self.status}"
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.is_called:
            self.status = Status.objects.get(name="now-serving")
            self.called_at = timezone.now()
        if self.queue_no is None:
            self.queue_no, self.queue_code = get_queue_no_and_code(self)
        super(Queue, self).save(*args, **kwargs)
    
    def get_current_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
    
    def get_current_waiting_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
    
    def get_current_now_serving_queues(branch_id):
        return Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="now-serving").id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
    
# ---------------------- RECEIVER ---------------------- #
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver([post_save, post_delete], sender=Queue)
def ws_notify_waiting_queues(sender, instance, **kwargs):
    branch = instance.branch
    
    channel_layer = get_channel_layer()
    group_name = f"waiting-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "waiting"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)

@receiver([post_save, post_delete], sender=Queue)
def ws_notify_now_serving_queues(sender, instance, **kwargs):
    branch = instance.branch
    
    channel_layer = get_channel_layer()
    group_name = f"now-serving-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "now-serving"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)
    
@receiver([post_save, post_delete], sender=Queue)
def ws_notify_current_stats(sender, instance, **kwargs):
    branch = instance.branch
    
    channel_layer = get_channel_layer()
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
    
    channel_layer = get_channel_layer()
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
    
    if instance.is_called:
        window = Window.objects.get(id=instance.window_id)
        
        channel_layer = get_channel_layer()
        group_name = f"call-queue-{branch.id}"
        event = {
            "type": "queue.call",
            "name": applicant_name,
            "window_name": window.name,
            "queue_code": queue_code
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
        
        instance.is_called = False
        instance.save()
    
@receiver([post_save], sender=Queue)
def ws_notify_current_tourism_total(sender, instance, **kwargs):
    branch = instance.branch
    
    channel_layer = get_channel_layer()
    group_name = f"current-tourism-stat-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "queue_status": "current-tourism-stat"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)