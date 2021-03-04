from django.urls import path
from MoonTrekBlog.views import BlogPostAll, BlogPostSingle


app_name = 'blog'

urlpatterns = [
    path('MTBlog/', BlogPostAll.as_view(), name = 'blogHome'),
    path('MTBlog/<slug:slug>/', BlogPostSingle.as_view(), name = 'blogPost'),
]