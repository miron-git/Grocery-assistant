from django.forms import ModelForm
from .models import Recipe, RecipeIngredient,Tag
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'text', 'tag', 'image', 'time', 'ingredient']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['breakfast', 'lunch', 'dinner']
# class RecipeIngredientForm(forms.ModelForm):

#     class Meta:
#         model = RecipeIngredient
#         fields = ['recipe', 'weight', 'ingredient']