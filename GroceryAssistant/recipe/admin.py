from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Tag

class RecipeAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "title", "author") 
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = ("-пусто-") 

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "weight", 'ingredient') 

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "unit") 

class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "breakfast", "lunch", "dinner")
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)