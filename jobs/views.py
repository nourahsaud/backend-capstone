from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Jobs
from user.models import CompanyProfile
from .serializers import JobsSerializer, JobsSerializerView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core import serializers

# Add New job
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_job(request: Request):

    '''
        This function is to add a new job.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = CompanyProfile.objects.get(user=user)
    request.data.update(company=profile.id)
    new_job = JobsSerializer(data=request.data)
    if new_job.is_valid():
        new_job.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "employee" : new_job.data
        }
        return Response(dataResponse)
    else:
        print(new_job.errors)
        dataResponse = {"msg" : "couldn't create an employee!"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get All jobs
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_jobs(request : Request):
    '''
        This function is to view all jobs.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    job = Jobs.objects.all()
    dataResponse = {
        "msg" : "List of all jobs",
        "jobs" : JobsSerializerView(instance=job, many=True).data
        }
    return Response(dataResponse)

# Get Company ID Jobs
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getCompanyJobs(request : Request):
    '''list the company's employees'''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)    
        
    profile = CompanyProfile.objects.get(user=user)
    jobs = Jobs.objects.filter(company= profile.id)
    dataResponse = {
        "msg" : "List of All company employees",
        "employees" : JobsSerializerView(instance=jobs, many=True).data
        }
    return Response(dataResponse)

# Delete ID Employee
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_job(request: Request, job_id):
    '''
        delete an employee
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    job = Jobs.objects.get(id=job_id) 
    job.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def edit_job(request : Request, job_id):
    '''
        Update Employee info
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    job = Jobs.objects.get(id=job_id)
    request.data.update(user=request.user.id)
    updated_job = JobsSerializer(instance=job, data=request.data)
    if updated_job.is_valid():
        updated_job.save()
        responseData = {
            "msg" : "updated successefully"
        }
        return Response(responseData)
    else:
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)
