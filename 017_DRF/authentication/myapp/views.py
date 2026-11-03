from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from myapp.serializer import *

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    ser = Userserializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"data":ser.data})
    else:
        return Response({"errors":ser.errors})
    

@api_view(['GET'])
@permission_classes([AllowAny])
def normal_user(request):
    return Response("Normal user")


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_user(request):
    return Response("admin user")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authenticated_user(request):
    return Response("authenticated user")