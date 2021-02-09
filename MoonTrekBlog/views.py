from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPostAll(ListView):
    model = BlogPost

class BlogPostSingle(DetailView):
    model = BlogPost
