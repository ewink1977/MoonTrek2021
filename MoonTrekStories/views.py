from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib import messages
from MoonTrekBlog.models import BlogPost
from MoonTrekStories.models import MoonTrekStories, MoonTrekChapters, Comment
from MoonTrekStories.dicts import seriesNames

def addComment(request, id):
    if request.method == 'POST':
        currentStory = MoonTrekStories.objects.get(id = id)
        NewComment = Comment.objects.create(
            commentor = request.POST['commentor'],
            comment = request.POST['comment'],
            story = currentStory,
            )
        NewComment.save()
        messages.success(request, 'Comment successfully added!')
        return render(request, 'MoonTrekStories/comment-return.html', {'comments': Comment.objects.filter(story = currentStory)})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'stories:storyHome'))

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
        thisStory = MoonTrekStories.objects.get(id = self.object.pk)
        context['comments'] = Comment.objects.filter(story = thisStory)
        # self.request.session['lastStoryID'] = self.object.pk
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