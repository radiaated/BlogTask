from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import Token
JWT_authenticator = JWTAuthentication()

def is_loggedin(func):

    def wrapper(request):
        print(request.COOKIES)
        try:
            x = JWT_authenticator.get_validated_token(request.COOKIES.get("access"))
        except:
            return Response({"details": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        # token = Token(token=x, verify=True)
        user = JWT_authenticator.get_user(x)

        if user:
            request.user = user
            return func(request)
        else:
            return Response({"details": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
    return wrapper
