from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, Product, User, Tag
from api.models import Favorite, Purchase
from .forms import RecipeForm
from .utils import get_dict_ingredients
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Sum


# @login_required
def index(request):
    recipe_list = Recipe.objects.all().order_by('-pub_date')
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    # tags = Tag.objects.get(id=2).recipe_set.all
    context = {'page': page, 'paginator': paginator}
    # if request.user.is_authenticated:
    #     favorite_list = Recipe.objects.filter(recipes_favorites__user=request.user)
    #     purchase_list = Recipe.objects.filter(recipes_purchases__user=request.user)
    #     return render(request, 'recipe/indexAuth.html', {'page': page, 
    #                                                     'paginator': paginator, 'purchase_list': purchase_list,})
    # else:
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
        Ingredient.objects.filter(recipe=recipe).delete()
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
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
    # favorite_list = Recipe.objects.filter(recipes_favorites__user=request.user)
    subscribe_list = User.objects.filter(authors__subscriber_id=request.user)
    return render(request,'recipe/singlePage.html', {'recipe': recipe, 'subscribe_list': subscribe_list})

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

def profile(request, username):
    profile = get_object_or_404(User, username=username)
    recipe_list = Recipe.objects.filter(author=profile.id)
    return render(request, 'recipe/authorRecipe.html', {'recipe_list': recipe_list, 'profile': profile})

def getShoplist(request):
    items = ''
    text = (Recipe.objects.filter(recipes_purchases__user=request.user)
        .values('ingredients__title', 'ingredients__dimension')
        .annotate(quantity=Sum('quantity__quantity'))
    )
#['ingredients__title'] ['ingredients__dimension'] ['quantity']
    for item in text:
        items += (f"{item['ingredients__title']}"
            f" \u2014 {item['quantity']}"
            f"{item['ingredients__dimension']} \n"
        )

    response = HttpResponse(items,
        content_type='text/plane',
        headers={'Content-Disposition': 'attachment; filename="ShopList.txt"'},
    )

    return response

def page_not_found(request, exception):
    #  Переменная exception содержит отладку
    return render(
        request, 
        "misc/404.html", 
        {"path": request.path}, 
        status=404
    )

def server_error(request):
    return render(request, "misc/500.html", status=500)