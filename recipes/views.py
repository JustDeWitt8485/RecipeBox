from django.shortcuts import render, reverse, HttpResponseRedirect

from recipes.models import Author, Recipes

from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.


def index(request):
    return render(request, 'index.html', {
        "recipes": Recipes.objects.all(), "authors": Author.objects.all()

        }
    )


def recipe_detail(request, recipe_id):
    the_recipe = Recipes.objects.get(id=recipe_id)
    return render(
        request, "recipe_detail.html", {"recipe": the_recipe}
    )


def add_recipe(request):
    html = "generic_form.html"

    if request.method == "POST":
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
    return render(request, html, {"form": form})


def author_detail(request, author_id):
    the_author = Author.objects.get(id=author_id)
    return render(
        request, "author_detail.html", {"author": the_author}
    )


def add_author(request):
    html = "generic_form.html"
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                email=data['email'],

            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, html, {"form": form})
