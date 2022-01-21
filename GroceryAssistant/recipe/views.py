from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient, Product
from api.models import Favorite
from .forms import RecipeForm
from .utils import get_dict_ingredients


def index(request):
    recipe_list = Recipe.objects.all().order_by("-pub_date")
    favorites_list = Recipe.objects.filter(recipes_favorites__user=request.user)

    return render(request, 'recipe/indexAuth.html', {'recipe_list': recipe_list, 'favorites_list': favorites_list})

def recipe_new(request):
    # if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES or None)
        ingredients = get_dict_ingredients(request)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for key, value in ingredients.items():
                product = get_object_or_404(Product, title=key)
                recipe_ing = Ingredient(recipe=recipe, product=product, quantity=value)
                recipe_ing.save()
            form.save_m2m()
            return redirect('index')
        return render(request, 'recipe/formRecipe.html', {'form': form})

def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request,'recipe/singlePage.html', {'recipe': recipe})

def favorites(request):
    favorites_list = Recipe.objects.filter(recipes_favorites__user_id=request.user)
    return render(request, 'recipe/favorite.html', {'favorites_list': favorites_list})

def tags(request, id):
    recipes = Recipe.objects.filter(tag=id)
    return render(request)

def subscriptions(request):
    pass