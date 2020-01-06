from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignupFormView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL), name="logout"),
    path('profile/', views.profile, name='profile'),

]