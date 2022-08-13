import imp
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User


def send_otp_email(email):
    subject = 'Account Verification Email - Clean Gist'
    otp = random.randint(1000, 9999)
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user = User.objects.get(email= email)
    user.otp = otp
    user.save()

