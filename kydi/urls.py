from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
import accounts
from rest_framework.authtoken import views
from accounts.serializers import CustomAuthToken

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('register/complete', accounts.views.django_registration_complete, name='django_registration_complete'),
    path('activate/complete', accounts.views.django_activation_complete, name='django_registration_activation_complete'),
    path('api-token-auth/', CustomAuthToken.as_view()),
    re_path(r'^favicon\.ico$', favicon_view),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)