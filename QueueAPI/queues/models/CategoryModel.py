from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    display_name = models.CharField(max_length=50, blank=False, null=False)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return f"{self.name} - {self.branch}"