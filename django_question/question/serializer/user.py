from rest_framework import serializers
from django.contrib.auth.models import User
import uuid
import string
import random

def x():
    strings = string.ascii_lowercase
    return ''.join(random.choice(strings) for i in range(10,20))

class BaseUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)

    def create(self, validated_data):
        user = User(username=x(),first_name=validated_data.get('first_name'),last_name=validated_data.get('last_name'),password="123456")
        user.set_password("123456")
        user.save()
        return user

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id']