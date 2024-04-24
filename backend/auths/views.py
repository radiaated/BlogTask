
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .utils import get_tokens_for_user
from django.db.models import Q
from .serializers import is_loggedin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

import json

# Create your views here.
class DecoratedTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
  
        request.data["refresh"] = request.COOKIES.get("refresh")

        response = super().post(request, *args, **kwargs)

        resp_data = response.data

        response.set_cookie("access", resp_data['access'], 60*60*24, secure=False)
        response.set_cookie("refresh", resp_data['refresh'], 60*60*24, secure=False, path="/auth/refresh/")
    
        return response




@api_view(["POST"])
def login(request):
    
    user = User.objects.filter(
            Q(username=request.data['username']) |
            Q(email=request.data['username'])
        )
    exists_user = user.exists()
    if not exists_user:
        return Response({"detail": "User don't exist."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not user[0].check_password(request.data['password']):
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
    print("uwu")
    tokens = get_tokens_for_user(user[0])

    response = Response({"access": tokens['access'], "refresh": tokens['access']})

    response.set_cookie("access", tokens['access'], 60*60*24, secure=False)
    response.set_cookie("refresh", tokens['refresh'], 60*60*24, secure=False, path="/auth/refresh/")
    
    return response


@api_view(["POST"])
def register(request):

    post_data=request.data

    if User.objects.filter(email=post_data['email']).exists():
        return Response({"detail": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=post_data['username']).exists():
        return Response({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    

    user = User.objects.create(
        first_name=post_data['first_name'],
        email=post_data['email'],
        username=post_data['username'],
        password=make_password(post_data['password'])
        )
    
    
    
    if user:
        user.save()

    serializers = UserSerializer(user)

    return Response(serializers.data, status=status.HTTP_201_CREATED)