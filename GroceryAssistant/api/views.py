from django.shortcuts import render
from recipe.models import Recipe, Ingredient, Tag, Product
from .models import Favorite
from .serializers import ProductSerializer, FavoriteSerializer
from rest_framework import generics, filters
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth import get_user_model

class APIProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

class APIFavorite(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        favorite = Favorite.objects.filter(recipe_id=id, user_id=request.user)
        favorite.delete()
        #т.к JS ждет "success": true/false
        return Response({"success": bool(favorite.delete())})

class APISubscriptions(APIView):
    def post(self, request):
        pass