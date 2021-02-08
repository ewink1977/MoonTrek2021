from django.shortcuts import render, redirect
from django.views import View

def IndexView(request):
    return render(request, 'html/baseIndex.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'html/contact.html', {'pagetitle': 'Moon Trek | Contact ewink!'})
    
    def post(self, request):
        pass
