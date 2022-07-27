from rest_framework import serializers
from .models import Employee , Favorite , RequestEmployee
from user.serializers import ProfileSerializer


class EmployeesSerializer(serializers.ModelSerializer):
    """For Serializing Employees"""
    class Meta :
        model = Employee
        fields = '__all__'

class EmployeesSerializerView(serializers.ModelSerializer):
    """For Serializing Employees"""
    company = ProfileSerializer()
    class Meta :
        model = Employee
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    """For Serializing Favorite"""
    class Meta :
        model = Favorite
        fields = '__all__'

class FavoriteSerializerView(serializers.ModelSerializer):
    """For Serializing Favorite"""
    class Meta :
        model = Favorite
        fields = '__all__'

class RequestEmployeeSerializer(serializers.ModelSerializer):
    """For Serializing Employee Requests"""
    class Meta :
        model = RequestEmployee
        fields = '__all__'


class RequestEmployeeSerializerView(serializers.ModelSerializer):
    """For Serializing Employee Requests"""
    company = ProfileSerializer()
    employee = EmployeesSerializer()
    class Meta :
        model = RequestEmployee
        fields = '__all__'