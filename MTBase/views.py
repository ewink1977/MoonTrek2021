import json
import urllib
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
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
            # ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            print(result)
            # ''' End reCAPTCHA validation '''
            if result['success'] == True:
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
                messages.error(request, 'Invalid reCAPTCHA. Please try again.', extra_tags = 'danger')
                return render(request, 'html/contact.html', context)
        else:
            context = {
                'pagetitle': 'Moon Trek | Contact ewink!',
                'form': form
            }
            messages.error(request, 'Something has gone wrong. Can you please try again?', extra_tags = 'danger')
            return render(request, 'html/contact.html', context)

def error_404_view(request, exception):
    return render(request, 'html/404.html')
