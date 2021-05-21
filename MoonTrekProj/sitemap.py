from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from MoonTrekBlog.models import BlogPost
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MoonTrekStories.models import MoonTrekStories
from MTBase.models import Profile

class StaticSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return ['base:landingPage', 'base:contactPage', 'LCARS:lcarsHome', 'stories:storyHome']
    
    def location(self, item):
        return reverse(item)

class ProfileSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Profile.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
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