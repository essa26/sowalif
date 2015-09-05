from django import forms
from django.core.validators import RegexValidator

from main.models import Cereal, NutritionFacts

alpha_numeric_validator = RegexValidator('^[a-zA-Z0-9_]+$', 'only letters and numbers')

class TagSearch(forms.Form):
	name = forms.CharField(required=True, validators=[letter_validator, number_validator])


class CreateTag(forms.ModelForm):
	class Meta:
		model = Tag
		# fields = '__all__'
		fields = ['name', 'post']