from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #flatpages
    path('about/', include('django.contrib.flatpages.urls')),
    path("auth/", include("users.urls")),
    #если нужного шаблона для /auth не нашлось в файле users.urls — 
    #ищем совпадения в файле django.contrib.auth.urls
    path("auth/", include("django.contrib.auth.urls")),
    path('api/', include('api.urls')),
    path('', include('recipe.urls')),
]

urlpatterns += [
        path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)