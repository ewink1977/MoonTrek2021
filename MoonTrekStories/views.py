from django.shortcuts import render, redirect 
from MoonTrekBlog.models import BlogPost

def storyHome(request):
    context = {
        'posts': BlogPost.objects.all(),
        'pagetitle': 'Moon Trek | Stories Home Page'
    }
    return render(request, 'html/storyHome.html', context)
