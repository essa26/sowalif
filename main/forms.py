from django import forms
from django.core.validators import RegexValidator
from main.models import Post, Comment
from main.models import Tag

alpha_numeric_validator = RegexValidator('^[a-zA-Z0-9_]+$', 'only letters and numbers')

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


class TagSearch(forms.Form):
    name = forms.CharField(required=True, validators=[alpha_numeric_validator])


class TagCreate(forms.ModelForm):
    class Meta:
        model = Tag
        # fields = '__all__'
        fields = ['name']


class UserSignup(forms.Form):
    username = forms.CharField(required=True, validators=[letter_validator])
    password = forms.CharField(widget=forms.PasswordInput())


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class CreatePost(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea())
    date_created = forms.DateTimeField()
    # tags =


class Comment_On(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
