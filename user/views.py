from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from .models import CompanyProfile 
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, ProfileSerializer


@api_view(['POST'])
def Register(request: Request):
    '''
        This function is to Register a new user.
    '''
    RegisterUser = UserRegisterSerializer(data=request.data)
    if RegisterUser.is_valid():
        new_user = User.objects.create_user(**RegisterUser.data)
        new_user.save()
        return Response({"msg": "created user successfuly"})
    else:
        print(RegisterUser.errors)
        return Response({"msg": "Couldn't create a suer"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Login(request : Request):
    '''
        This function is for the user login.
    '''
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            #create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)


    return Response({"msg" : "please provide a valid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def CompanyInfo(request: Request, profile_id):
    '''
        This function is to view all employees.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    profile = CompanyProfile.objects.filter(pk=profile_id)
    dataResponse = {
        "msg" : "List of all employees",
        "profile" : ProfileSerializer(instance=profile, many=True).data
        }
    return Response(dataResponse)
