from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', views.register, name='register'),
    path('custom-registration', views.custom_registration, name='custom_registration'),
    path('register/complete', views.django_registration_complete, name='django_registration_complete'),
]