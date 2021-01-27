from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))

