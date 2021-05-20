from django.contrib.sitemaps import Sitemap
from MoonTrekBlog.models import BlogPost
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MoonTrekStories.models import MoonTrekStories

class BlogSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

class StorySiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return MoonTrekStories.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

class LCARSCharSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Character.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

class LCARSShipiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Ship.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

class LCARSMiscSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return PlacesAndItems.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at