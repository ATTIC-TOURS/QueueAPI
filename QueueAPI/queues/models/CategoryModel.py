from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return f"{self.name} - {self.branch}"