from django.shortcuts import render
from recipe.models import Recipe, Ingredient, Tag, Product
from .models import Favorite, Subscription, Purchase
from .serializers import ProductSerializer, FavoriteSerializer, SubscribeSerializer, PurchaseSerializer 
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

class APISubscription(APIView):
    def post(self, request):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(subscriber=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        subscribe = Subscription.objects.filter(subscriber_id=request.user, author_id=id)
        subscribe.delete()
        return Response({"success": bool(subscribe.delete())})

class APIPurchase(APIView):

    def get(self, request):
       pass

    def post(self, request):
        serializer = PurchaseSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        purchase = Purchase.objects.filter(user_id=request.user, recipe_id=id)
        purchase.delete()
        return Response({"success": bool(purchase.delete())})
