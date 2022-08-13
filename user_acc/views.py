import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import LogInSerializer, UserSerializer, VerifyAccountSerializer, LogOffSerializer
from .emails import *

# Create your views here.

class RegisterUser(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            
            if serializer.is_valid():
                
                serializer.save()
                send_otp_email(serializer.data['email'])
                return Response({"status": 200,
                    'message': 'Check EMail',
                    'data': serializer.data,
                    })
            else:
                
                return Response({'status': 400,
                    'message': 'Something Wrong',
                    'data': serializer.errors})

        except Exception as e:
            print(e)
            return Response({'status': 400,
                'message': 'Exception',
                'data': serializer.errors})

class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data = data)
            if serializer.is_valid():
                email= serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email= email)
                print(user[0].otp)
                if not user.exists():
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'invalid Email'})

                if user[0].otp != otp:
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'Wrong OTP'})
            
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({'status': 200, 'message': 'Account Verified', 'data': serializer.data})  
        except Exception as e:
            print(e)
            return Response({'status': 400,
                'message': 'Exception',
                'data': serializer.errors})

class UserLogIn(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LogInSerializer(data = data)
            if serializer.is_valid():
                email= serializer.data['email']
                password = serializer.data['password']
                user = User.objects.filter(email= email)
                print(user[0].password)
                if not user.exists():
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'invalid Email'})

                if user[0].password != password:
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'Wrong Password'})

                if user[0].is_loggedin == True:
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'User is Already Logged In'})
            
                user = user.first()
                user.is_loggedin = True
                user.save()
                return Response({'status': 200, 'message': 'Logged In', 'data': serializer.data})
            else:
                return Response({'status': 400,
                'message': 'Seliazer',
                'data': serializer.errors})
                
        except Exception as e:
            print(e)
            return Response({'status': 400,
                'message': 'Exception',
                'data': serializer.errors})

class UserLogOff(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LogOffSerializer(data = data)
            if serializer.is_valid():
                email= serializer.data['email']
                user = User.objects.filter(email= email)
                print(user)
                if user[0].is_loggedin != True:
                    return Response({'status': 400,
                        'message': 'Something Wrong',
                        'data': 'User is Not Logged In'})
            
                user = user.first()
                user.is_loggedin = False
                user.save()
                return Response({'status': 200, 'message': 'Logged Off', 'data': serializer.data})
            else:
                return Response({'status': 400,
                'message': 'Seliazer',
                'data': serializer.errors})
                
        except Exception as e:
            print(e)
            return Response({'status': 400,
                'message': 'Exception',
                'data': serializer.errors})