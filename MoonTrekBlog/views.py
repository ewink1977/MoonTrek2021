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

# <app>/<model>_<type>.html