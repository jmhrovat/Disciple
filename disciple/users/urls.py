from . import views

from django.urls import path

urlpatterns = [
     path('sign_up', views.sign_up, name='sign_up')
     # path('logout', views.logout_view, name='logout_view'),
     # path('login', views.login_view, name='login_view')
]
