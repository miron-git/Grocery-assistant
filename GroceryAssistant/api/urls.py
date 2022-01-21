from django.urls import path, include
from .views import APIProduct, APIFavorite, APISubscriptions
from api import views

urlpatterns = [
    path('ingredients/', APIProduct.as_view()),
    path('favorites/', APIFavorite.as_view()),
    path('favorites/<int:id>/', APIFavorite.as_view()),
    path('subscriptions/', APISubscriptions.as_view()),
    path('subscriptions/<int:id>/', APISubscriptions.as_view()),
]