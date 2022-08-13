from dataclasses import fields
import email
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified', 'is_loggedin']



class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    

class LogOffSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_loggedin = serializers.BooleanField(default=False)