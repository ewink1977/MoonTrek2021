from django.db import models
from django.urls import reverse
from django.db.models import Q
from tinymce.models import HTMLField


class StoryQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                        Q(summary__icontains=query)|
                        Q(description__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
class StoryManager(models.Manager):
    def get_queryset(self):
        return StoryQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class MoonTrekStories(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(default = 'placeholder.jpg',
        upload_to = 'storyIMG')
    fullStoryPDF = models.FileField(upload_to = 'full_stories/PDF/', null = True)
    fullStoryEPUB = models.FileField(upload_to = 'full_stories/EPUB/', null = True)
    series = models.IntegerField()
    position = models.IntegerField()
    summary = HTMLField()
    description = models.CharField(max_length = 255, default = "Please replace me.")
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = StoryManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stories:storyPage', kwargs={'slug': self.slug})

class MoonTrekChapters(models.Model):
    chapter_number = models.IntegerField()
    title = models.CharField(max_length = 255)
    content = HTMLField()
    epilogue = models.BooleanField(default = False)
    slug = models.SlugField()
    story = models.ForeignKey(MoonTrekStories, 
        related_name = 'chapters', 
        on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.story.title} : Chapter {self.chapter_number} - {self.title}"

    def get_absolute_url(self):
        return reverse('stories:chapterPage', kwargs={'slug': self.slug, 'story_slug': self.story.slug})

class Comment(models.Model):
    commentor = models.CharField(max_length = 255)
    comment = models.TextField(max_length = 200)
    story = models.ForeignKey(MoonTrekStories,
        related_name = 'comment', 
        on_delete = models.CASCADE)
    is_admin = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'Comment for {self.story.title}'