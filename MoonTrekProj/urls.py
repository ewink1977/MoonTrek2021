from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSiteMap, StorySiteMap, LCARSCharSiteMap, LCARSMiscSiteMap, LCARSShipiteMap, StaticSiteMap, ProfileSiteMap

urlpatterns = [
    path('', include('MTBase.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('MoonTrekBlog.urls')),
    path('LCARS/', include('MoonTrekLCARS.urls')),
    path('stories/', include('MoonTrekStories.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': { 'blog': BlogSiteMap, 
    'stories': StorySiteMap, 'lcarsChar': LCARSCharSiteMap, 
    'lcarsShip': LCARSShipiteMap, 'lcarsMisc': LCARSMiscSiteMap, 
    'static': StaticSiteMap, 'profile': ProfileSiteMap} },
    name='django.contrib.sitemaps.views.sitemap'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'MTBase.views.error_404_view'