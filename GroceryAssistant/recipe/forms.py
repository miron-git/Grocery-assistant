from django.forms import ModelForm
from .models import Recipe, RecipeIngredient,Tag
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'time', 'image', 'tag', ]
        widgets = {'tag': forms.CheckboxSelectMultiple}
        #'ingredient'