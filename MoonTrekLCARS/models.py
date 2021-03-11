from typing import Tuple
from django.db import models
from django.db.models.fields import SlugField
from tinymce.models import HTMLField
from MoonTrekStories.models import MoonTrekStories

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

    def __str__(self):
        return f'Character: { self.name }'

class Ship(models.Model):
    name = models.CharField(max_length = 255)
    faction = models.IntegerField(default = 0)
    content = HTMLField()
    slug = models.SlugField()
    created_at =  models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    story = models.ManyToManyField(MoonTrekStories, 
        related_name = 'ships', blank = True)

    def __str__(self):
        return f'Ship: { self.name }'

class PlacesAndItems(models.Model):
    name = models.CharField(max_length = 255)
    type = models.IntegerField(default = 0)
    content = HTMLField()
    slug = SlugField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    story = models.ManyToManyField(MoonTrekStories, 
        related_name = 'places', blank = True)

    def __str__(self):
        return f'Place/Item: { self.name }'