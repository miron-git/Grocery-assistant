from django.urls import path, include
from .views import APIIngredient

urlpatterns = [
    path('ingredients/', APIIngredient.as_view()),
]