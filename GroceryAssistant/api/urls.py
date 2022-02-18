from django.urls import path, include
from .views import APIProduct, APIFavorite, APISubscription, APIPurchase
from api import views

urlpatterns = [
    path('ingredients/', APIProduct.as_view()),
    path('favorites/', APIFavorite.as_view()),
    path('favorites/<int:id>/', APIFavorite.as_view()),
    path('subscriptions/', APISubscription.as_view()),
    path('subscriptions/<int:id>/', APISubscription.as_view()),
    path('purchases/', APIPurchase.as_view()),
    path('purchases/<int:id>/', APIPurchase.as_view()),
]