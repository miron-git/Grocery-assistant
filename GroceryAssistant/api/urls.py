from django.urls import path, include
from .views import APIProduct

urlpatterns = [
    path('ingredients/', APIProduct.as_view()),
]