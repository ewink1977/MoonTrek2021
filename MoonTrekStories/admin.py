from django.contrib import admin
from MoonTrekStories.models import MoonTrekStories, MoonTrekChapters


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'series')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter_number')

admin.site.register(MoonTrekStories, StoryAdmin)
admin.site.register(MoonTrekChapters, ChapterAdmin)
