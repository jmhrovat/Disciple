from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input_field '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input_field '}))