from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "rounded-md border-green-500", "placeholder": "Your URL to shorten"}))
    
    class Meta:
        model = Shortener
        fields = ('long_url',)
