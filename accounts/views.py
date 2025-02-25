import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import main

def django_registration_complete(request):
    return render(request, 'django_registration/registration_complete.html')

def django_activation_complete(request):
    return render(request, 'django_registration/activation_complete.html')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        context = {}
        print(username, email)
        try:
            user_code = f'{username[0:4]}/{username[4:]}'
            member = main.models.Member.objects.get(code=user_code)
            return redirect("/accounts/register/")
        except main.models.Member.DoesNotExist:
            context["errors"] = "User Does Not Exist"
    else:
        context = {}
        

    return render(request, 'accounts/start_registration.html', context)