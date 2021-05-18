from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from tinymce.models import HTMLField
from MoonTrekStories.models import MoonTrekStories
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems

class BlogQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                        Q(content__icontains=query)|
                        Q(tags__icontains=query) |
                        Q(slug__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    content = HTMLField()
    tags = models.CharField(max_length = 255, default = '', blank = True)
    date_posted = models.DateTimeField(default = timezone.now)
    slug = models.SlugField(null = False, unique = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(
        User, 
        related_name = 'blog_post',
        on_delete = models.CASCADE
    )

    related_story = models.ManyToManyField(
        MoonTrekStories, 
        related_name = 'blog_post',
        blank = True
    )

    related_character = models.ManyToManyField(
        Character,
        related_name = 'blog_post', 
        blank = True
    )

    related_ship = models.ManyToManyField(
        Ship, 
        related_name = 'blog_post', 
        blank = True
    )

    related_place = models.ManyToManyField(
        PlacesAndItems,
        related_name = 'blog_post',
        blank = True
    )

    objects = BlogManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blogPost', kwargs={'slug': self.slug})
