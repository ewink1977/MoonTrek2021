from django.urls import path
from MoonTrekStories import views as StoryViews

app_name = 'stories'

urlpatterns = [
    path('', StoryViews.storyHome, name = 'storyHome'),
    path('<slug:slug>/', StoryViews.StoryPage.as_view(), name = 'storyPage'),
    path('<slug:story_slug>/<slug:slug>/', StoryViews.ChapterPage.as_view(), name = 'chapterPage'),
]