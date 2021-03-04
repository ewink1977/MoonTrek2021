from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from MoonTrekBlog.models import BlogPost

class BlogPostAll(ListView):
    paginate_by = 3
    model = BlogPost
    ordering = ['-date_posted']

class BlogPostSingle(DetailView):
    model = BlogPost

# <app>/<model>_<type>.html