from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee, Favorite, RequestEmployee
from .serializers import EmployeesSerializer, FavoriteSerializer, RequestEmployeeloyeeSerializer
from user.models import CompanyProfile


# Add New Employee 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def addEmployee(request: Request):
    ''' 
        This function is to add a new employee.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = CompanyProfile.objects.get(user=user)
    request.data.update(company=profile.id)
    new_employee = EmployeesSerializer(data=request.data)
    if new_employee.is_valid():
        new_employee.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "employee" : new_employee.data
        }
        return Response(dataResponse)
    else:
        print(new_employee.errors)
        dataResponse = {"msg" : "couldn't create an employee!"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get All Employees
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getEmployee(request : Request):
    ''' 
        This function is to view all employees.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    emps = Employee.objects.all()
    dataResponse = {
        "msg" : "List of all employees",
        "employees" : EmployeesSerializer(instance=emps, many=True).data
        }
    return Response(dataResponse)

# Get Company ID Employees
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getCompanyEmployee(request : Request, profile_id):
    '''list the company's employees'''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)    
    
    emps = Employee.objects.filter(company= profile_id)
    dataResponse = {
        "msg" : "List of All company employees",
        "employees" : EmployeesSerializer(instance=emps, many=True).data
        }
    return Response(dataResponse)

# Update ID Employee
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def editEmployee(request : Request, emp_id):
    '''
        Update Employee info
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = CompanyProfile.objects.get(user=user)
    
    emp = Employee.objects.get(id=emp_id)
    request.data.update(company=profile.id)
    updated_emp = EmployeesSerializer(instance=emp, data=request.data)
    if updated_emp.is_valid():
        updated_emp.save()
        responseData = {
            "msg" : "updated successefully"
        }
        return Response(responseData)
    else:
        print(updated_emp.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

# Delete ID Employee
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def deleteEmployee(request: Request, emp_id):
    '''
        delete an employee
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    emp = Employee.objects.get(id=emp_id) 
    emp.delete()
    return Response({"msg" : "Deleted Successfully"})

# Get Employee by ID
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getEmp(request : Request , employee_id):
    '''
        This function is to view all employees.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    employee = Employee.objects.filter(pk=employee_id)
    dataResponse = {
        "msg" : "List of all employees",
        "employees" : EmployeesSerializer(instance=employee, many=True).data
        }
    return Response(dataResponse)

# _______________________________________________________

# Add New Request 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_req(request:Request, emp_id):
    '''
        This function is to add new request
    '''
    user:User = request.user
    emp = Employee.objects.get(id=emp_id)
    profile = CompanyProfile.objects.get(user=user)
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if RequestEmployee.objects.filter(company=profile.id, employee=emp).exists():
         return Response({"msg" : "You have already sent a request !"}, status=status.HTTP_400_BAD_REQUEST)

    request.data.update(company=profile.id, employee=emp.id)

    if Employee.objects.filter(company=profile.id).exists() :
        return Response({"msg" : "Not Allowed, you cannot requset your own employees"}, status=status.HTTP_401_UNAUTHORIZED)
    

    new_req = RequestEmployeeloyeeSerializer(data=request.data)
    if new_req.is_valid():
        new_req.save()
        dataResponse = {
        "msg" : "Created Successfully",
        "req" : new_req.data
        }
        return Response(dataResponse)
    else:
        print(new_req.errors)
        dataResponse = {"msg" : "couldn't add a request"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get Company ID Request - sent
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_sent(request: Request, profile_id):
    ''' 
    This function is to list all of the requests
    '''

    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    req = RequestEmployee.objects.filter(company= profile_id)
    dataResponse = {
        "msg" : "List of employees requests",
        "req" : RequestEmployeeloyeeSerializer(instance=req, many=True).data
    }

    return Response(dataResponse)

# Get Company ID Request - recived 
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_received(request: Request, profile_id):
    ''' 
    This function is to list all of the requests
    '''

    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    req = RequestEmployee.objects.filter(employee__company= profile_id)

    dataResponse = {
        "msg" : "List of employees requests",
        "req" : RequestEmployeeloyeeSerializer(instance=req, many=True).data
    }

    return Response(dataResponse)

# Delete ID Request
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_req(request: Request, req_id):
    '''
        Delete a request
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    req = RequestEmployee.objects.get(id=req_id) 
    req.delete()

    return Response({"msg" : "Deleted Successfully"})

# Add Fav 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_fav(request:Request, emp_id):
    '''
        This function is to add new request
    '''
    user:User = request.user
    emp = Employee.objects.get(id=emp_id)
    profile = CompanyProfile.objects.get(user=user)
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if Favorite.objects.filter(company=profile.id, employee=emp).exists():
         return Response({"msg" : "You have already sent a request !"}, status=status.HTTP_400_BAD_REQUEST)

    request.data.update(company=profile.id, employee=emp.id)

    if Employee.objects.filter(company=profile.id).exists() :
        return Response({"msg" : "Not Allowed, you cannot requset your own employees"}, status=status.HTTP_401_UNAUTHORIZED)
    

    new_fav = FavoriteSerializer(data=request.data)
    if new_fav.is_valid():
        new_fav.save()
        dataResponse = {
        "msg" : "Created Successfully",
        "req" : new_fav.data
        }
        return Response(dataResponse)
    else:
        print(new_fav.errors)
        dataResponse = {"msg" : "couldn't add a request"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get Fav
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_fav(request: Request, profile_id):
    ''' 
    This function is to list all of the requests
    '''

    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    fav = Favorite.objects.filter(company= profile_id)
    dataResponse = {
        "msg" : "List of employees requests",
        "req" : FavoriteSerializer(instance=fav, many=True).data
    }

    return Response(dataResponse)

# Delete fav
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_fav(request: Request, fav_id):
    '''
        delete an employee
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    fav = Favorite.objects.get(id=fav_id) 
    fav.delete()
    return Response({"msg" : "Deleted Successfully"})