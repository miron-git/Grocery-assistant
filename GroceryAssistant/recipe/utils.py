from recipe.models import Recipe
from decimal import Decimal

def get_dict_ingredients(request):
    ingredients = {}
    for key, ingredient_name in request.POST.items():
        if 'nameIngredient' in key:
            _ = key.split('_')
            ingredients[ingredient_name] = Decimal(request.POST[f'valueIngredient_{_[1]}'].replace(',', '.'))
    return ingredients
