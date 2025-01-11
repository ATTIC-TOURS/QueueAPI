# ---------------------- RECEIVER ---------------------- #
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from queues.models import Queue


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
    group_name = f"in-progress-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "branch_id": branch.id,
        "queue_status": "in-progress"
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
    name = instance.name
    queue_code = instance.code
    
    if instance.is_called:
        window = Window.objects.get(id=instance.window_id)
        
        channel_layer = get_channel_layer()
        group_name = f"call-queue-{branch.id}"
        event = {
            "type": "queue.call",
            "name": name,
            "window_name": window.name,
            "queue_code": queue_code
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
        
        queue = Queue.objects.get(id=instance.id)
        queue.is_called = False
        queue.save()