from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Recipe, Ingredient, Tag, Product
from django import forms


User = get_user_model()

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'time', 'image', 'tags']
        widgets = {'tags': forms.CheckboxSelectMultiple}
    