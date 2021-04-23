from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('MTBase.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('MoonTrekBlog.urls')),
    path('LCARS/', include('MoonTrekLCARS.urls')),
    path('stories/', include('MoonTrekStories.urls')),
    path('tinymce/', include('tinymce.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)