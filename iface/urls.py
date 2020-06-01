from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from iface import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('create_dataset', app_views.create_dataset),
    path('trainer', app_views.trainer),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)