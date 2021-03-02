from django.contrib import admin
from MoonTrekStories.models import MoonTrekStories, MoonTrekChapters


class StoryAdmin(admin.ModelAdmin):
    list_display = ('series', 'title')
    prepopulated_fields = {'slug': ('title',)}

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_number', 'title')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(MoonTrekStories, StoryAdmin)
admin.site.register(MoonTrekChapters, ChapterAdmin)
