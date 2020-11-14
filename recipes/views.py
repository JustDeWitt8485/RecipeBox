from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipes.models import Author, Recipes
from recipes.forms import AddAuthorForm, AddRecipeForm, LoginForm

# Create your views here.


def index(request):
    return render(request, 'index.html', {
        'recipes': Recipes.objects.all(), 'authors': Author.objects.all()

    }
    )


@login_required
def recipe_detail(request, recipe_id):
    the_recipe = Recipes.objects.get(id=recipe_id)
    return render(
        request, 'recipe_detail.html', {'recipe': the_recipe}
    )


@login_required
def add_recipe(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data['title'],
                body=data['body'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()
    return render(request, html, {'form': form})


@login_required
def author_detail(request, author_id):
    the_author = Author.objects.get(id=author_id)
    return render(
        request, 'author_detail.html', {'author': the_author}
    )


@staff_member_required
@login_required
def add_author(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            Author.objects.create(
                name=data['name'],
                email=data['email'],
                user=new_user,
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, html, {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})
