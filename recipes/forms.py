from django import forms

from recipes.models import Author


class AddAuthorForm(forms.Form):

    name = forms.CharField(max_length=50)
    email = forms.EmailField()


class AddRecipeForm(forms.Form):

    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
