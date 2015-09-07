from django import forms
from django.core.validators import RegexValidator

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


class UserSignup(forms.Form):
    username = forms.CharField(required=True, validators=[letter_validator])
    password = forms.CharField(widget=forms.PasswordInput())


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
