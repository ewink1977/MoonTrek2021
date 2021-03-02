from django.shortcuts import render
from django.core.paginator import Paginator
from MoonTrekBlog.models import BlogPost

def storyHome(request):
    blogPosts = BlogPost.objects.all().order_by('-date_posted')
    paginator = Paginator(blogPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'pagetitle': 'Moon Trek | Stories Home Page'
    }
    return render(request, 'html/storyHome.html', context)

def storyPage(request):
    pass

def chapterPage(request):
    pass

# <app>/<model>_<type>.html