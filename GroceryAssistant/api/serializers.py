from rest_framework import serializers
from recipe.models import RecipeIngredient, Recipe, Tag, Ingredient

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'dimension')
        model = Ingredient