from django.urls import path
from MoonTrekStories import views

app_name = 'stories'

urlpatterns = [
    path('', views.storyHome, name = 'storyHome'),
]