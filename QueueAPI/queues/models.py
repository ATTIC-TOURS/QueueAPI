from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    
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
    error_msg = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.id}-{self.is_active}"


class Mobile(models.Model):
    mac_address = models.CharField(max_length=100, blank=False, null=False)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.branch_id}-{self.mac_address}"
    

class Queue(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, blank=False, null=False)
    window_id = models.ForeignKey(Window, on_delete=models.CASCADE, blank=True, null=True)
    queue_no =  models.PositiveIntegerField(blank=False, null=False)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, null=False)
    is_called = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)