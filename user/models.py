from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    avatar = models.URLField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username