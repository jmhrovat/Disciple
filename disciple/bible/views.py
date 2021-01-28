from django.shortcuts import render

# Create your views here.
def bible_navigation(request):
    return render(request, 'bible/navigation.html')