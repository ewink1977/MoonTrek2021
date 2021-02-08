from django.shortcuts import render, redirect 

def buffer(request):
    return render(request, 'html/baseIndex.html')
