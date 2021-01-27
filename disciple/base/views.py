from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    else:
        return render(request, 'base/index.html')
