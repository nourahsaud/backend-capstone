from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CompanyProfile

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'avatar', 'bio']
