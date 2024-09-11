from django.urls import path, include
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    path('',views.home, name='home'),
    path('crear/', FlightCreateView.as_view(), name = 'crear'),
    
]