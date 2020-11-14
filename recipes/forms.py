from django import forms

from recipes.models import Author


class AddAuthorForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):

    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
