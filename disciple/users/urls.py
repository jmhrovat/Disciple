from . import views
from users.views import *

from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
     path('sign_up', views.SignUpView.as_view()),
     path('login', LoginView.as_view(), name='login')
]
