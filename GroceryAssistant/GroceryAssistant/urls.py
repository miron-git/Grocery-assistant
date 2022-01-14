from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #  регистрация и авторизация
    path("auth/", include("users.urls")),
    #  если нужного шаблона для /auth не нашлось в файле users.urls — 
    #  ищем совпадения в файле django.contrib.auth.urls
    path("auth/", include("django.contrib.auth.urls")),
    path('', include('recipe.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)