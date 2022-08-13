from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import create_profile, update_profile, profile, getRoutes

urlpatterns = [
    path('', getRoutes),
    path('profile/', create_profile),
    path('profilelist/', profile),
    path('update-profile/<id>/', update_profile),
    
]