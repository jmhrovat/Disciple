from . import views
from users.views import *

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm


urlpatterns = [
     path('', views.user_home, name='user_home'),
     path('sign_up', views.SignUpView.as_view()),
     path('login', LoginView.as_view(authentication_form=LoginForm), name='login'),
     path('logout', LogoutView.as_view(), name='logout')
]
