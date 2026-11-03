from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class Userserializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
    def create(self, validated_data):
        
        password = validated_data.pop('password')
        u = User.objects.create_user(password=password,**validated_data)
        return u