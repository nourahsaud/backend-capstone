from django.db import models

class Jobs(models.Model):
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    adddate = models.DateTimeField(auto_now=True)