from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
]

#Этот код будет работать, когда ваш сайт в режиме отладки.
# Он позволяет обращаться файлам в директории, указанной в MEDIA_ROOT по имени, через префикс MEDIA_URL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)