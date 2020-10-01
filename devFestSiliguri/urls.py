"""devFestSiliguri URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.urls import path , include
from myapp.views import notification, apiendpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notification', notification),
    path('api/',apiendpoint),
]
