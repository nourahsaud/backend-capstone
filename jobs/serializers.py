from rest_framework import serializers
from .models import Jobs
from user.serializers import ProfileSerializer


class JobsSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = Jobs
        fields = '__all__'


class JobsSerializerView(serializers.ModelSerializer):
    """For Serializing Employees"""
    company = ProfileSerializer()
    class Meta :
        model = Jobs
        fields = '__all__'