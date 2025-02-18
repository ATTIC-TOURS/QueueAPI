from django.db import models


class Marquee(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE)
    text = models.CharField(max_length=200)  
    
    def __str__(self):
        return self.text[:50]