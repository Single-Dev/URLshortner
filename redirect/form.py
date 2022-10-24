from django import forms
from redirect.models import *

class ShortnerFrom(forms.ModelForm):
    class Meta:
        model = UrlShortner
        fields = "__all__"