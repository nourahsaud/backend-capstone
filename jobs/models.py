from django.db import models
from user.models import CompanyProfile


class Jobs(models.Model):
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    current_date = models.DateTimeField(auto_now=True, blank=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
