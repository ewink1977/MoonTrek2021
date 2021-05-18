from django.db import models
from django.db.models.fields import SlugField
from django.db.models import Q
from django.urls import reverse
from tinymce.models import HTMLField
from MoonTrekStories.models import MoonTrekStories

class CharacterQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                        Q(content__icontains=query)|
                        Q(slug__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
class CharacterManager(models.Manager):
    def get_queryset(self):
        return CharacterQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Character(models.Model):
    name = models.CharField(max_length = 255)
    faction = models.IntegerField(default = 0)
    rankIMG = models.ImageField(upload_to = 'rankIMG/', blank = True)
    department = models.IntegerField(default = 0)
    content = HTMLField()
    slug = models.SlugField()
    created_at =  models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    story = models.ManyToManyField(MoonTrekStories, 
        related_name = 'characters', blank = True)
    
    objects = CharacterManager()

    def __str__(self):
        return f'Character: { self.name }'
    
    def get_absolute_url(self):
        return reverse('LCARS:characterView', kwargs={'slug': self.slug})

class ShipQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                        Q(content__icontains=query)|
                        Q(slug__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
class ShipManager(models.Manager):
    def get_queryset(self):
        return ShipQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Ship(models.Model):
    name = models.CharField(max_length = 255)
    faction = models.IntegerField(default = 0)
    content = HTMLField()
    slug = models.SlugField()
    created_at =  models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    story = models.ManyToManyField(MoonTrekStories, 
        related_name = 'ships', blank = True)
    
    objects = ShipManager()

    def __str__(self):
        return f'Ship: { self.name }'
    
    def get_absolute_url(self):
        return reverse('LCARS:shipView', kwargs={'slug': self.slug})

class MiscQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                        Q(content__icontains=query) |
                        Q(slug__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
class MiscManager(models.Manager):
    def get_queryset(self):
        return MiscQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
class PlacesAndItems(models.Model):
    name = models.CharField(max_length = 255)
    type = models.IntegerField(default = 0)
    content = HTMLField()
    slug = SlugField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = MiscManager()

    story = models.ManyToManyField(MoonTrekStories, 
        related_name = 'places', blank = True)

    def __str__(self):
        return f'Place/Item: { self.name }'
    
    def get_absolute_url(self):
        return reverse('LCARS:miscView', kwargs={'slug': self.slug})