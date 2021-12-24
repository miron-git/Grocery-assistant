from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

def index(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipe_list': recipe_list})

def recipe_new(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('index')
        return render(request, 'recipe/formRecipe.html', {'form': form})
    form = RecipeForm()
    return render(request, 'recipe/formRecipe.html', {'form': form})
