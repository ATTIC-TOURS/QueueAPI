from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"