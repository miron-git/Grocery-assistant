from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient, Product
from .forms import RecipeForm
from .utils import get_dict_ingredients


def index(request):
    recipe_list = Recipe.objects.all()
    recipe_ingr = Ingredient.objects.all()
  
    return render(request, 'recipe/indexAuth.html', {'recipe_list': recipe_list, 'recipe_ingr': recipe_ingr})

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
    # form = RecipeForm()
    # return render(request, 'recipe/formRecipe.html', {'form': form})
