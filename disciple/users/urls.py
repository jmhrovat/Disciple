from . import views
from users.views import *

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm


urlpatterns = [
     path('', views.user_home_view, name='user_home'),
     path('register', views.register, name='register'),
     path('login', LoginView.as_view(authentication_form=LoginForm), name='login'),
     path('logout', LogoutView.as_view(), name='logout')
]
