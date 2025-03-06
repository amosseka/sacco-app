import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_registration.forms import RegistrationForm
from django_registration.backends.activation.views import RegistrationView
from django.http import HttpResponse
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
        
        try:
            User.objects.get(username=username)
            context["errors"] = "A user with that username already exists"
        except:
            try:
                user_code = f'{username[0:4]}/{username[4:]}'
                member = main.models.Member.objects.get(code=user_code)
                if member.email_address == email:
                    return redirect(f"/accounts/register?username={username}&email={email}")
                else:
                    context["errors"] = "Email does not exist"
            except main.models.Member.DoesNotExist:
                context["errors"] = "User Does Not Exist"
    else:
        context = {}
        

    return render(request, 'accounts/start_registration.html', context)


def custom_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            return HttpResponse("200 OK")
    else:
        username = request.GET.get("username")
        email = request.GET.get("email")
        form = RegistrationForm(initial={"username": username, "email": email})
    context = {
        "form": form
    }

    return render(request, "accounts/custom_registration.html", context)


class CustomRegistrationView(RegistrationView):
    pass