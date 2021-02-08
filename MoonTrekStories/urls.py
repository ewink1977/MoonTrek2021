from django.urls import path
from MoonTrekStories import views

urlpatterns = [
    path('', views.buffer),
]