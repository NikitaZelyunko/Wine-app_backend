from django.shortcuts import render
from .models import CustomUser
from vine.models import VineItem
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token 
from django.contrib import auth

# Create your views here.
@api_view(['POST'])
def register(request):
    email=request.data['email']
    if CustomUser.objects.filter(email__iexact=email).exists():
        return Response({'c':'error','d':'exist'},status=400)
    serializer=CustomUserSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        from django.contrib.auth.hashers import make_password
        serializer.save(email=email, password=make_password(request.data['password']))
        user=CustomUser.objects.get(email=request.data['email'])
        Token.objects.create(user=user)
        return Response({'status':'success'},status=201)
    else:
        return Response({'c':'error','d':'data is not valid'},status=400)

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password=request.data['password']
    user=auth.authenticate(email=email,password=password)
    if user:
        auth.login(request,user)
        serializer=CustomUserSerializer(user)
        response_data={'token':user.auth_token.key}
        return Response(response_data,status=200)
    elif CustomUser.objects.filter(email=email, is_active=False).exists():
        return Response({'c':'error','d':'inactive'},status=401)
    else:
        return Response({'c':'error','d':'not_exist'},status=401)

@api_view(['POST'])
def edit_user(request):
    print(request.data['first_name'])
    if request.user.is_authenticated:
        user=request.auth.user
        serializer=CustomUserSerializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('OK',status=200)
        return Response(serializer.error_messages, status=200)
    return Response('ERROR',status=400)

@api_view(['GET'])
def logout(request):
    auth.logout(request)
    return Response('Logout',status=200)


        
        
        