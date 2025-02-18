from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "branches"
    
    def __str__(self):
        return self.name