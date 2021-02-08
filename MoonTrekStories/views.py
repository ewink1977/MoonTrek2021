from django.shortcuts import render, redirect 

def storyHome(request):
    return render(request, 'html/storyHome.html')
