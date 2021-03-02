from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from MoonTrekBlog.models import BlogPost
from MoonTrekStories.models import MoonTrekStories, MoonTrekChapters
from MoonTrekStories.dicts import seriesNames

def storyHome(request):
    blogPosts = BlogPost.objects.all().order_by('-date_posted')
    paginator = Paginator(blogPosts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    stories = MoonTrekStories.objects.all().order_by('series')
    context = {
        'page_obj': page_obj,
        'pagetitle': 'Moon Trek | Stories Home Page',
        'stories': stories,
        'series': seriesNames,
    }
    return render(request, 'html/storyHome.html', context)

class StoryPage(DetailView):
    model = MoonTrekStories

def storyPage(request):
    pass

def chapterPage(request, story_slug, chap_slug):
    chapter = MoonTrekChapters.objects.get(slug = chap_slug)
    pass

# <app>/<model>_<type>.html