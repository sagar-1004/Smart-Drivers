from django.urls import path, include

from .views import *
from backend.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', home, name="home"),

]
