from pyexpat import model
from django import forms
from redirect.models import URLshortner

class ShortnerFrom(forms.ModelForm):
    class Meta:
        model = URLshortner
        fields = "__all__"