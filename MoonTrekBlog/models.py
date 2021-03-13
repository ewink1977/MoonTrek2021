from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from MoonTrekStories.models import MoonTrekStories

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogPost', kwargs={'slug': self.slug})
