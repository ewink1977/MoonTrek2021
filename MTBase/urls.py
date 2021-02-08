from django.urls import path
from MTBase import views

urlpatterns = [
    path('', views.IndexView, name = 'mainPage'),
]