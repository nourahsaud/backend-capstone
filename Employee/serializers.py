from rest_framework import serializers
from .models import Employee , Favorite , RequestEmployee


class EmployeesSerializer(serializers.ModelSerializer):
    """For Serializing Employees"""
    class Meta :
        model = Employee
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    """For Serializing Favorite"""
    class Meta :
        model = Favorite
        fields = '__all__'

class RequestEmployeeloyeeSerializer(serializers.ModelSerializer):
    """For Serializing Employee Requests"""
    class Meta :
        model = RequestEmployee
        fields = '__all__'