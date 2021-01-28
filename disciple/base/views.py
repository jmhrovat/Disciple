from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('bible_navigation')
    else:
        return render(request, 'base/index.html')
