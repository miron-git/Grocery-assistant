from django.db import models
from django.contrib.auth import get_user_model
from recipe.models import Recipe

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт', related_name='recipes_favorites') 

    class Meta:
        unique_together = ['user', 'recipe']

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик', related_name='subscribers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='authors')

    class Meta:
        unique_together = ['author', 'subscriber']

class Purchase(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт', related_name='recipes_purchases') 
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'recipe']
