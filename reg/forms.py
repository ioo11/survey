from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import (
    UserCreationForm,
)

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'date_of_birth',
            'fname',
            'lname',
            'sex',
            'country',
            'sity',
        )
