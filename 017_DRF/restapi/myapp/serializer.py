from rest_framework.serializers import ModelSerializer
from myapp.models import *

class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        # fields='__all__'
        # fields=['name']
        exclude=['name']
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
    
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'