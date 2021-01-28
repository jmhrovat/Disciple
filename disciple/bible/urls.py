from . import views
from users.views import *

from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm


urlpatterns = [
     path('', views.bible_navigation, name='bible_navigation'),
]
