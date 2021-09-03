from django.template import Template, RequestContext
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from MoonTrekBlog.models import BlogPost

class BlogPostAll(ListView):
    paginate_by = 5
    model = BlogPost
    ordering = ['-date_posted']

class BlogPostSingle(DetailView):
    model = BlogPost
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(BlogPostSingle, self).get_context_data(**kwargs)
        self.object.urlSafe = Template(self.object.content).render(RequestContext(self.request, context))

        return context

# <app>/<model>_<type>.html