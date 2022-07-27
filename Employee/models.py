from django.db import models
from user.models import CompanyProfile
from django.contrib.auth.models import User

class Employee(models.Model):
    name =models.CharField(max_length=50)
    avatar = models.URLField(default=None)
    position = models.CharField(max_length=50, default=None)
    linkedin = models.URLField(default=None)
    state = models.BooleanField(default=False)
    current_date = models.DateField(auto_now_add=True , blank=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class RequestEmployee(models.Model):
    Choices = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),   
        ('Waiting', 'Waiting')
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE) 
    #request_status = models.CharField(max_length=10 , choices = Choices)
    


class Favorite(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
