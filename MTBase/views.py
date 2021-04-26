from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from MTBase.forms import ContactForm

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
        form = ContactForm()
        context = {
            'pagetitle': 'Moon Trek | Contact ewink!',
            'form': form
        }
        return render(request, 'html/contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = f"FROM : { form.cleaned_data['senderName'] } at { form.cleaned_data['senderEmail'] } \n \n MESSAGE : { form.cleaned_data['senderMessage'] } \n \n Regards, Moon Trek Contact Bot."
            send_mail('A Contact From The Moon Trek Contact Form!', 
            message, 
            'moontrek@douglasavenue.com', 
            ['otakuphotog@gmail.com'],
            fail_silently = False)
            messages.success(request, 'Thanks! The contact form has been sent via internet magic to Erin! If you gave us your contact info, he will get back with you soon!')
            return redirect('stories:storyHome')
        else:
            context = {
                'pagetitle': 'Moon Trek | Contact ewink!',
                'form': form
            }
            messages.error(request, 'Something has gone wrong. Can you please try again?', extra_tags = 'danger')
            return render(request, 'html/contact.html', context)

def error_404_view(request, exception):
    return render(request, 'html/404.html')
