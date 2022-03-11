from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_time, validate_file_size
User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Название')
    dimension = models.CharField(max_length=20, verbose_name = 'Единицы измерения')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = 'Ингредиент')
    quantity = models.IntegerField(verbose_name = 'Вес') 
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name = 'quantity', verbose_name = 'Рецепт')

    def __str__(self):
        return self.product, self.quantity
        

class Tag(models.Model):
    tag = models.CharField(max_length=50, verbose_name = 'Тэг')

    def __str__(self):
        return self.tag

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name = 'Название рецепта')
    description = models.TextField(verbose_name = 'Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(upload_to='recipes/', validators=[validate_file_size])
    time = models.PositiveIntegerField(verbose_name = 'Время приготовления', validators=[validate_time])
    tags = models.ManyToManyField(Tag, verbose_name = 'Тег')
    ingredients = models.ManyToManyField(Product, through = Ingredient, verbose_name = 'Ингредиент блюда')
    
    # slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

