from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов,
# добавляем к ним фильтр
from api.models import Purchase, Favorite
register = template.Library()


@register.filter 
def addclass(field, css):
        return field.as_widget(attrs={"class": css})

@register.filter
def in_shopping(value, user):
    return Purchase.objects.filter(recipe=value, user=user).exists()

@register.filter
def favorite_list(value, user):
    return Favorite.objects.filter(recipe=value, user=user)

