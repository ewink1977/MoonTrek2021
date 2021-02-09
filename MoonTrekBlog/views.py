from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import BlogPost

class BlogPostAll(ListView):
    paginate_by = 10
    model = BlogPost
    ordering = ['-date_posted']

class BlogPostSingle(DetailView):
    model = BlogPost

# <app>/<model>_<type>.html