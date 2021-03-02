from django.urls import path
from MoonTrekStories import views as StoryViews

app_name = 'stories'

urlpatterns = [
    path('', StoryViews.storyHome, name = 'storyHome'),
    path('<slug:story_slug>/', StoryViews.storyPage, name = 'storyPage'),
    path('<slug:story_slug>/<int:chap_num>/<slug:chap_slug>/', StoryViews.chapterPage, name = 'chapterPage'),
]