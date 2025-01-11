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
    
    def __str__(self):
        return f"{self.branch.name}-{self.code}-{self.name}-{self.created_at}"

class MarkQueue(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)  
    
    def __str__(self):
        branch_name = Branch.objects.get(pk=self.branch_id_id).name
        return f"{branch_name}-{self.text}"