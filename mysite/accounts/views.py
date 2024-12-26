from django.shortcuts import render
from .serializers import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics 
from .models import UserProfile
from .serializers import UserProfileSerializeer, RegistraionSerializer
from .permissions import IsUser

# Create your views here.

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        else: 
            email = serializer.data['email']
            password = serializer.data['password']
            
            user = authenticate(email=email,password=password)
            if user:
                token , _ =Token.objects.get_or_create(user=user)
                return Response({
                    "status" : True,
                    "data": {'token': str(token)}
                })
            else:
                 return Response({
                    "status" : False,
                    "data": {},
                    "message": "Invalid credentials"
                })
                 
                 
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({
                    "status" : True,
                    "data": {},
                    "message": "Logout successfull"
                })
        
@api_view(['POST'])
def register(request):
    
    if request.method == 'POST':
        serializer = RegistraionSerializer(data = request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successfull"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data) 
    
class ProfileDetail(APIView):
    permission_classes = [IsUser]
    
    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except:
            return Response(status=404)
        serializer = UserProfileSerializeer(profile)
        return Response(serializer.data)
    
    def put(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except:
            return Response(status=404)
        serializer = UserProfileSerializeer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else: 
            return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except:
            return Response(status=404)
        profile.delete()
        return Response(status=204)