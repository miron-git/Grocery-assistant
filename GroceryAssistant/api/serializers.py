from rest_framework import serializers
from recipe.models import Ingredient, Recipe, Tag, Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'dimension')
        model = Product