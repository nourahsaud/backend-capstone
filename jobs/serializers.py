from rest_framework import serializers
from .models import Jobs


class JobsSerializer(serializers.ModelSerializer):
    """For Serializing Comment"""
    class Meta :
        model = Jobs
        fields = '__all__'