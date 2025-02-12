from django.db import models
from django.utils import timezone
from queues.models import Window


class Queue(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=False, null=False)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, blank=False, null=False)
    service_type = models.CharField(max_length=50, blank=True, null=True)
    window = models.ForeignKey("Window", on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, blank=False, null=False)
    queue_code = models.CharField(max_length=10, blank=True, null=True)
    applicant_name = models.CharField(max_length=50, blank=False, null=False)
    no_applicant = models.PositiveIntegerField(blank=True, null=True)
    applicant_type = models.CharField(max_length=50, blank=True, null=True)
    is_senior_pwd = models.BooleanField(default=False, blank=False, null=False)
    queue_no =  models.PositiveIntegerField(blank=False, null=False)
    coordinator_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    called_at = models.DateTimeField(blank=True, null=True)
    is_called = models.BooleanField(default=False, blank=False, null=False)    
    is_priority = models.BooleanField(default=False, blank=False, null=False)    
    
    def __str__(self):
        return f"{self.service} - {self.pax} - {self.name} - {self.code} - {self.status}"
    
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
        
        queue = Queue.objects.get(id=instance.id)
        queue.is_called = False
        queue.save()
    
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