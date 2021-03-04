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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seriesNames'] = seriesNames
        return context

class ChapterPage(DetailView):
    model = MoonTrekChapters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seriesNames'] = seriesNames
        allChapters = self.get_queryset()
        context['allChapters'] = allChapters
        return context

# <app>/<model>_<type>.html