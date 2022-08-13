from email.policy import default
from django.db import models
from user_acc.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    current_city = models.TextField(max_length=256, blank=True)
    home_town = models.TextField(max_length=256, blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    school= models.CharField(max_length=100, blank=True)
    contact_info = models.CharField(max_length=20, blank=True)
    realtionship_status = models.CharField(max_length=20, blank=True)
    dob = models.DateField(auto_now=True)
    profile_pic = models.ImageField(upload_to='profile_images', default="Blank_Profile_Pic.png")


    def __str__(self):
        return self.user_name
        
        