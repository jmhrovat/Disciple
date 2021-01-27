from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required



# Create your views here.
class SignUpView(View):
    def get(self, request):
        return render(request, 'users/index.html')


@login_required
def user_home_view(request):
    return render(request, 'users/home.html')

