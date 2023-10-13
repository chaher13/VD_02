from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
