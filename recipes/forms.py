from django import forms
from recipes.models import Author


class RecipeAddForm(forms.Form):
	title = forms.CharField(max_length=30)
	body = forms.CharField(widget=forms.Textarea)
	author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorAddForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = [
			'name',
			'bio'
		]


