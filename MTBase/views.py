from django.shortcuts import render, redirect
from django.views import View
# from .models import Profile
from django.contrib.auth.models import User

def IndexView(request):
    return render(request, 'html/baseIndex.html')

def profileView(request, user):
    userProfile = User.objects.get(username = user)
    context = {
        'user': userProfile
    }
    return render(request, 'html/profile.html', context)

class ContactView(View):
    def get(self, request):
        return render(request, 'html/contact.html', {'pagetitle': 'Moon Trek | Contact ewink!'})
    
    def post(self, request):
        pass

