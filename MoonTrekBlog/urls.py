from django.urls import path
from MoonTrekBlog.views import BlogPostAll, BlogPostSingle


app_name = 'blog'

urlpatterns = [
    path('', BlogPostAll.as_view(), name = 'blogHome'),
    path('<slug:slug>/', BlogPostSingle.as_view(), name = 'blogPost'),
]