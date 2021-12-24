from django.shortcuts import render
from recipe.models import Recipe, RecipeIngredient, Tag, Ingredient
#from rest_framework.views import APIView
#from rest_framework.response import Response
from .serializers import IngredientSerializer
from rest_framework import generics, filters
import django_filters.rest_framework



# class APIIngredient(APIView):
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title',]

#     def get(self, request):
#         ingredients = Ingredient.objects.all()
#         serializer = IngredientSerializer(ingredients,  many=True)
#         return Response(serializer.data)

class APIIngredient(generics.ListAPIView):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

