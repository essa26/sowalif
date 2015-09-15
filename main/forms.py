from django import forms
from django.core.validators import RegexValidator
from main.models import Post, Comment
#from main.models import Tag
from taggit.managers import TaggableManager
import datetime
from taggit.forms import *


alpha_numeric_validator = RegexValidator(
    '^[a-zA-Z0-9_]+$', 'only letters and numbers')

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')


class TagSearch(forms.Form):
    name = forms.CharField(required=True, validators=[alpha_numeric_validator])


class UserSignup(forms.Form):
    username = forms.CharField(required=True, validators=[letter_validator])
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class CreatePost(forms.Form):
    title = forms.CharField(required=True)
    #image = forms.ImageField(
        #label='Select an image', help_text='max. 42 megabytes', required=False)
    text = forms.CharField(widget=forms.Textarea())
    #image = forms.ImageField()
    tags = TagField()


class CommentOn(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
