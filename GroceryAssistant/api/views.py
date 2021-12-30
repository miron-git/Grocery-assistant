from django.shortcuts import render
from recipe.models import Recipe, Ingredient, Tag, Product
#from rest_framework.views import APIView
#from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import generics, filters
import django_filters.rest_framework



# class APIIngredient(APIView):
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title',]

#     def get(self, request):
#         ingredients = Ingredient.objects.all()
#         serializer = IngredientSerializer(ingredients,  many=True)
#         return Response(serializer.data)

class APIProduct(generics.ListAPIView):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

