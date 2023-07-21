from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ProjectRoad import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls'))
] # + static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)