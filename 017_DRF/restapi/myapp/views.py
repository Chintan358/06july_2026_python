from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

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
    return Response({"data":ser.data},status=status.HTTP_200_OK)


@api_view(['POST'])
def crate_student(request):
    ser =  StudentSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"msg":"Registration successsful","data":ser.data},status=status.HTTP_201_CREATED)
    else:
        return Response({"error":ser.errors},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def retrive_student(request,id):   
    try:
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_student(request,id):
    try :
        student = Student.objects.get(id=id)
        ser = StudentSerializer(student,request.data)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data,"message":"Updated successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])
def patch_student(request,id):
    try :
            student = Student.objects.get(id=id)
            ser = StudentSerializer(student,request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data,"message":"Updated successfully"},status=status.HTTP_201_CREATED)
            else:
                return Response({"erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
            return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student =  Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
    
    


class ProductView(APIView):
    
    def get(self,request):
        try:
            products = Product.objects.all()
            ser = ProductSerializer(products,many=True)
            return Response({"data":ser.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self,request):
        try:
            ser = ProductSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"something went wrong","erros":ser.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductViewById(APIView):
    
    def get(self,request,id):
        try:
            products = Product.objects.get(id=id)
            ser = ProductSerializer(products)
            return Response({"data":ser.data},status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message":"Product not found"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id):
        return Response("put api calling")
    
    def delete(self,request,id):
        return Response("delete api calling")
    
    
    
class EmployeeViewSet(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer