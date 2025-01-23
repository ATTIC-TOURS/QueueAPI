from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=False, null=False)
    notes = models.CharField(max_length=100, blank=True, null=True)
    is_cut_off = models.BooleanField(default=False, blank=False, null=False)
    quota = models.PositiveIntegerField(blank=True, null=True)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=False, null=False)