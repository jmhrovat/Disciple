from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from users.models import Profile
from django.contrib.auth import login



from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.get_user_from_credentials()

            if user:
                login(request, user)
                return redirect('user_home')

    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def user_home_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'users/home.html', context)

