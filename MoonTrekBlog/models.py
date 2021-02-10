from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    content = HTMLField()
    date_posted = models.DateTimeField(default = timezone.now)
    slug = models.SlugField(null = False, unique = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogPost', kwargs={'slug': self.slug})
