from django.urls import path
from .views import RegisterUser, VerifyOTP, UserLogIn, UserLogOff

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('login/', UserLogIn.as_view()),
    path('logoff/', UserLogOff.as_view()),
]