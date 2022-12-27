from django import forms
from redirect.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ShortnerFrom(forms.ModelForm):
    class Meta:
        model = UrlShortner
        fields = ['url',]

        from django.contrib.auth import get_user_model

