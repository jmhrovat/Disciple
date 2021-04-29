from django.shortcuts import render
from tasks.models import *

from django.views.generic import TemplateView


# Create your views here.
class TaskDashboardView(TemplateView):
    template_name = 'tasks/index.html'




