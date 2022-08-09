
from django.contrib import admin
from django.urls import path, input
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
