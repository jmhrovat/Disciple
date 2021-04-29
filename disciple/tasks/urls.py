from . import views
from tasks.views import *

from django.urls import path, include



urlpatterns = [
     path('', TaskDashboardView.as_view(), name='task_dashboard'),
]
