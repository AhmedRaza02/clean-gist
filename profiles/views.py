from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from django.contrib.auth.decorators import login_required
from user_acc.models import User
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Register new User with data sent in post request'
        },
        {
            'Endpoint': '/verify/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Verifies new User with OTP'
        },
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Allows User to log in with verified Credentials'
        },
        {
            'Endpoint': '/logoff/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Sets login to False'
        },
        {
            'Endpoint': '/profilelist/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of profile'
        },
        
        {
            'Endpoint': '/profile/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new profile with data sent in post request'
        },
        {
            'Endpoint': '/update-profile/',
            'method': 'PATCH',
            'body': {'body': ""},
            'description': 'Updates an existing profile with data sent in post request'
        },
    ]
    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@login_required
def profile(request):
    try:
        profiles =  Profile.objects.all()
        serializer = ProfileSerializer(profiles, many = True)

        print(serializer.data)
        return Response({"status": 200,
                    'data': serializer.data,
                    })
        
    except Exception as e:
        print(e)
        return Response({'status': 400,
                        'message': 'Exception',
                        'data': serializer.errors
                        })

@api_view(['POST'])
@login_required
def create_profile(self, request):
    try:
        data =  request.data
        serializer = ProfileSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"status": 200,
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
                        'data': serializer.errors
                        })
@api_view(['PATCH'])
@login_required
def update_profile(request, id):
    try:
        profile_obj = Profile.objects.get(user = id)
        data =  request.data
        serializer = ProfileSerializer(profile_obj, data = data, partial= True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"status": 200,
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
                        'data': serializer.errors
                        })


