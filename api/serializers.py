from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password 
class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=255)
    class Meta:
        model=User
        fields=['id','first_name','last_name','email','password','confirm_password']
    def validate(self, data):
        password=data.get('password')
        confirm_password=data.pop('confirm_password')
        if password !=confirm_password:
            raise serializers.ValidationError('password should match')
        return data
    def validate_password(self,value):
        return make_password(value)