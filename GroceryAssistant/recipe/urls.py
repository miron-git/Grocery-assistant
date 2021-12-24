from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
]
