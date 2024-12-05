# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form extending Django's UserCreationForm.
    Includes email and phone number fields.
    """
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False, max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', 'role')
