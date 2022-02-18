from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('recipe/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('favorites/', views.favorites, name='favorites'),
    path('tags/', views.tags, name='tags'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('recipe/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('purchases/', views.purchases, name='purchases')
]
