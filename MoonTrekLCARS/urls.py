from django.urls import path
from MoonTrekLCARS import views

urlpatterns = [
    path('', views.buffer),
]