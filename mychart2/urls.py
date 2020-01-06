from django.shortcuts import render
from . import views
from django.urls import path, include

app_name="mychart2"
urlpatterns = [
    path('', views.makechart, name='data_json'),
    path('comeon/', views.comeon, name='comeon')
]

# Create your views here.
