from django.urls import path
from MTBase import views

app_name = 'base'

urlpatterns = [
    path('', views.IndexView, name = 'landingPage'),
    path('contact/', views.ContactView.as_view(), name = 'contactPage'),
]