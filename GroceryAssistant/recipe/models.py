from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Ingredient(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Название')
    unit = models.CharField(max_length=20, verbose_name = 'Единицы измерения')

    def __str__(self):
        return f"{self.title}"

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name = 'Ингредиент')
    weight = models.IntegerField(verbose_name = 'Вес') 
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name = 'Рецепт')

    def __str__(self):
        return f"{self.ingredient}, {self.weight}"

class Tag(models.Model):
    breakfast = models.CharField(max_length=50, verbose_name = 'Завтрак')
    lunch = models.CharField(max_length=50, verbose_name = 'Обед')
    dinner = models.CharField(max_length=50, verbose_name = 'Ужин')

    def __str__(self):
        return f"{self.breakfast}"

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=50, verbose_name = 'Заголовок')
    text = models.TextField(verbose_name = 'Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    time = models.PositiveIntegerField(verbose_name = 'Время приготовления')
    tag = models.ManyToManyField(Tag, verbose_name = 'Тег')
    ingredient = models.ManyToManyField(Ingredient, through = RecipeIngredient, verbose_name = 'Ингредиент блюда')