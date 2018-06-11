from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, 
                        password=password)
    if user:
        login(request, user)
    else:
        data = dict(errMsg='Invalid username or password', 
                    'errCode'='0')
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

def user_logout(request):
    logout(request)

