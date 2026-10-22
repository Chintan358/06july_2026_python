from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *

@api_view(['POST'])
def create(request):
    return Response("POST api calling")

@api_view(['GET'])
def list_data(request):
    return Response("GET api calling")

@api_view(['PUT'])
def update(request):
    return Response("PUT api calling")

@api_view(['DELETE'])
def destroy(request):
    return Response("DELETE api calling")


@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = StudentSerializer(students,many=True)
    return Response({"data":ser.data})


@api_view(['POST'])
def crate_student(request):
    ser =  StudentSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"msg":"Registration successsful"})
    else:
        return Response({"error":ser.errors})
    
@api_view(['GET'])
def retrive_student(request,id):
    
    try:
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"data":ser.data})
    except Student.DoesNotExist:
        return Response({"message":"Student not found"})
