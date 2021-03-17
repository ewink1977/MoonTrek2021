from django.contrib import admin
from MoonTrekStories.models import MoonTrekStories, MoonTrekChapters, Comment


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'series')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter_number', 'story', 'epilogue')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentor', 'story')

admin.site.register(MoonTrekStories, StoryAdmin)
admin.site.register(MoonTrekChapters, ChapterAdmin)
admin.site.register(Comment, CommentAdmin)
