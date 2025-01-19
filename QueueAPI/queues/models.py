from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    display_name = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class ServiceType(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "branches"
        
    def __str__(self):
        return self.name
    
class Window(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "statuses"
        
    def __str__(self):
        return self.name

class Printer(models.Model):
    mac_address = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    error_msg = models.CharField(max_length=200, blank=True, null=True)    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        label = "ACTIVE" if self.is_active else "INACTIVE"
        return f"{self.branch}-{label}"

class Mobile(models.Model):
    mac_address = models.CharField(max_length=100, blank=False, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    
    def __str__(self):
        label = "ACTIVE" if self.is_active else "INACTIVE"
        return f"{self.branch}-{self.mac_address}-{label}"
    
class Queue(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=False, null=False)
    window = models.ForeignKey(Window, on_delete=models.CASCADE, blank=True, null=True)
    queue_no =  models.PositiveIntegerField(blank=False, null=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, null=False)
    is_called = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    is_senior_pwd = models.BooleanField(default=False, blank=False, null=False)
    pax = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    def __str__(self):
        return f"{self.branch.name}-{self.code}-{self.name}-{self.created_at}"

class MarkQueue(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)  
    
    def __str__(self):
        branch_name = Branch.objects.get(pk=self.branch_id_id).name
        return f"{branch_name}-{self.text}"
    
    


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
    
@receiver([post_save], sender=Queue)
def ws_notify_current_tourism_total(sender, instance, **kwargs):
    branch = instance.branch
    
    channel_layer = get_channel_layer()
    group_name = f"current-tourism-total-queue-{branch.id}"
    event = {
        "type": "queues.update",
        "queue_status": "current-tourism-total"
    }
    async_to_sync(channel_layer.group_send)(group_name, event)