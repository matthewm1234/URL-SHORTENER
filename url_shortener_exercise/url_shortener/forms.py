from django import forms


class ShortenURLForm(forms.Form):
    original_url = forms.URLField()
