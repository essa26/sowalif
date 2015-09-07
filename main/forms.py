from django import forms
from django.core.validators import RegexValidator
from main.models import Post, Comment

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


class UserSignup(forms.Form):
    username = forms.CharField(required=True, validators=[letter_validator])
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class Create_Post(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea())
    date_created = forms.DateTimeField()
    tags =


class Comment_On(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

