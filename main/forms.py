from django import forms
from django.core.validators import RegexValidator
from main.models import Post, Comment
#from main.models import Tag
from taggit.managers import TaggableManager
import datetime
from taggit.forms import *



alpha_numeric_validator = RegexValidator('^[a-zA-Z0-9_]+$', 'only letters and numbers')

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
    text = forms.CharField(widget=forms.Textarea())
    tags = TagField()


class CommentOn(forms.Form):
    text = forms.CharField(widget=forms.Textarea())


