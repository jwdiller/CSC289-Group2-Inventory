from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile

class cssThemeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cssTheme']
        widgets = {
            'cssTheme': forms.RadioSelect
        }

# Initializes email field and creates form field values
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PasswordUserChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'cssTheme']
        widgets = {
            'cssTheme': forms.RadioSelect
        }