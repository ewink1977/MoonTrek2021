from django.core import paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from MoonTrekBlog.models import BlogPost

def storyHome(request):
    blogPosts = BlogPost.objects.all()
    paginator = Paginator(blogPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'pagetitle': 'Moon Trek | Stories Home Page'
    }
    return render(request, 'html/storyHome.html', context)
