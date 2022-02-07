from django.contrib import admin
from .models import Recipe, Ingredient, Product, Tag

class RecipeAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "name", 'time', "author", "description", "image") 
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = ("-пусто-")
    # prepopulated_fields = {'slug': ('name',)} 

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "quantity") 

class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "dimension") 

class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "tag")
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)