from django import forms
from django.core.validators import RegexValidator

alpha_numeric_validator = RegexValidator('^[a-zA-Z0-9_]+$', 'only letters and numbers')

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')

class TagSearch(forms.Form):
	name = forms.CharField(required=True, validators=[letter_validator, number_validator])


class CreateTag(forms.ModelForm):
	class Meta:
		model = Tag
		# fields = '__all__'
		fields = ['name', 'post']


class UserSignup(forms.Form):
    username = forms.CharField(required=True, validators=[letter_validator])
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
