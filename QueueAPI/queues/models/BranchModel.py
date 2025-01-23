from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "branches"