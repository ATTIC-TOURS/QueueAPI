from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)
    notes = models.CharField(max_length=100, blank=True, null=True)
    is_cut_off = models.BooleanField(default=False)
    quota = models.PositiveIntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.branch}"