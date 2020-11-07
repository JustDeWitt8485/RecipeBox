from django.shortcuts import render

from recipes.models import Author, Recipes

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
