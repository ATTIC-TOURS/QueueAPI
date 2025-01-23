from django.db import models


class Marquee(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)  