from django.shortcuts import render

# Create your views here.
def portal():

    return render(request, 'base/portal/index.html')
