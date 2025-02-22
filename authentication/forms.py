from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
