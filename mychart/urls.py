from django.urls import path
from . import views

app_name='mychart'
urlpatterns = [
    path('', views.index, name='index'),
    path('data.json/', views.data_json, name='data_json'),
]