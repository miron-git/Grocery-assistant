from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, Product, User
from api.models import Favorite, Purchase
from .forms import RecipeForm
from .utils import get_dict_ingredients
from django.core.paginator import Paginator

# @login_required
def index(request):
    recipe_list = Recipe.objects.all().order_by('-pub_date').all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    context = {'page': page, 'paginator': paginator}
    if request.user.is_authenticated:
        favorite_list = Recipe.objects.filter(recipes_favorites__user=request.user)
        purchase_list = Recipe.objects.filter(recipes_purchases__user=request.user)
        return render(request, 'recipe/indexAuth.html', {'favorite_list': favorite_list, 'page': page, 'paginator': paginator, 'purchase_list': purchase_list})
    else:
        return render(request, 'recipe/indexAuth.html', context)

def recipe_new(request):
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

def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipe_view', recipe_id=recipe_id)
    
    form = RecipeForm(request.POST or None, files=request.FILES or None, instance=recipe)
    ingredients = get_dict_ingredients(request)
    for field in form.errors:
        print(field)
    if form.is_valid():
        print('test111111112')
        Ingredient.objects.filter(recipe=recipe).delete()
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        print('test111111111')
        for key, value in ingredients.items():
            product = get_object_or_404(Product, title=key)
            recipe_ing = Ingredient(recipe=recipe, product=product, quantity=value)
            recipe_ing.save()
        form.save_m2m()
        return redirect('recipe_view', recipe_id=recipe_id)
    return render(request, 'recipe/formChangeRecipe.html', {'form': form, 'recipe': recipe})

def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
        return redirect('index')
    return redirect('index')


def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    favorite_list = Recipe.objects.filter(recipes_favorites__user=request.user)
    subscribe_list = User.objects.filter(authors__subscriber_id=request.user)
    return render(request,'recipe/singlePage.html', {'recipe': recipe, 'favorite_list': favorite_list, 'subscribe_list': subscribe_list})

def favorites(request):
    favorites_list = Recipe.objects.filter(recipes_favorites__user_id=request.user)
    return render(request, 'recipe/favorite.html', {'favorites_list': favorites_list})

def tags(request, id):
    recipes = Recipe.objects.filter(tag=id)
    return render(request)

def subscriptions(request):
    user_list = User.objects.filter(authors__subscriber_id=request.user)
    recipe_list = Recipe.objects.filter(author__in=user_list)
    return render(request, 'recipe/myFollow.html', {'user_list': user_list, 'recipe_list': recipe_list})

def purchases(request):
    purchases_list = Recipe.objects.filter(recipes_purchases__user=request.user)
    return render(request, 'recipe/shopList.html', {'purchases_list': purchases_list})