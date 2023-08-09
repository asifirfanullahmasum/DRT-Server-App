from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trip
from django import forms

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['username', 'email', 'password1', 'password2']
