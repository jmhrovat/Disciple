from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.models import User
from users.models import Profile

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')
            else:
                print('user not found')
                user = User.objects.create(
                    username=username,
                    password=password,
                    first_name=first_name.capitalize(),
                    last_name=last_name.capitalize()
                )
                user.set_password(password)
                user.save()
                Profile.objects.create(user=user).save()

                login(request, user)
                return redirect('homepage')
            return redirect('register')
    else:
        f = SignUpForm()

    return render(request, 'registration/register.html', {'form': f})


@login_required
def user_home_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'users/home.html')

