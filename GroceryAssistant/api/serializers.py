from rest_framework import serializers
from recipe.models import Ingredient, Recipe, Tag, Product, User
from .models import Favorite, Subscription, Purchase
from django.contrib.auth import get_user_model


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'dimension')
        model = Product


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only = True)
    id = serializers.SlugRelatedField(slug_field='id', queryset=Recipe.objects.all(), source='recipe')

    class Meta:
        fields = ('user', 'id')
        model = Favorite


class SubscribeSerializer(serializers.ModelSerializer):
    subscriber = serializers.SlugRelatedField(slug_field='id', read_only = True)
    id = serializers.SlugRelatedField(slug_field='id', queryset=User.objects.all(), source='author')

    class Meta:
        fields = ('subscriber', 'id')
        model = Subscription


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.SlugRelatedField(slug_field='id', queryset=Recipe.objects.all(), source='recipe')
    user = serializers.SlugRelatedField(slug_field='id', read_only = True)

    class Meta:
        fields = ('id', 'user')
        model = Purchase
