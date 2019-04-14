from django import forms

class ShortenForm(forms.Form):
    original_link = forms.CharField(label="Your URL ")