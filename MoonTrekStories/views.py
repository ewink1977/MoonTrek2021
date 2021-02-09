from django.shortcuts import render, redirect 

# Dummy Data For Formatting.
# VVVVVVVVVVVVVVVVVVVVVVVVVV
nyaaBlog = [
    {
        'author': 'ewink',
        'title': 'This is a blog post!',
        'content': 'This is test content! Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, explicabo eius illum incidunt et laudantium labore voluptatibus! Nobis consectetur dignissimos sit praesentium non quia, eum facilis vitae doloribus. Cum, in?',
        'date_posted': 'January 31, 2021'
    },
    {
        'author': 'ewink',
        'title': 'A Second Post!',
        'content': 'The first 50 words or so... Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, explicabo eius illum incidunt et laudantium labore voluptatibus! Nobis consectetur dignissimos sit praesentium non quia, eum facilis vitae doloribus. Cum, in?',
        'date_posted': 'January 31, 2021'
    }
]
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# End Dummy Data

def storyHome(request):
    context = {
        'posts': nyaaBlog,
        'pagetitle': 'Moon Trek | Stories Home Page'
    }
    return render(request, 'html/storyHome.html', context)
