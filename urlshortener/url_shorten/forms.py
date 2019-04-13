from django import forms

class shorten_urls(forms.Form):
    original_link = forms.TextInput()