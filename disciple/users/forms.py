from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))

    def clean_data(self):
        self.username = self.cleaned_data['username']
        self.password = self.cleaned_data['password']
        self.first_name = self.cleaned_data['first_name']
        self.last_name = self.cleaned_data['last_name']

    def get_user_from_credentials(self):
        self.clean_data()
        user = authenticate(username=self.username, password=self.password)
        if user:
            return user
        else:
            user = User.objects.create(
                username=self.username,
                password=self.password,
                first_name=self.first_name.capitalize(),
                last_name=self.last_name.capitalize()
            )
            user.set_password(self.password)
            user.save()
            return user

