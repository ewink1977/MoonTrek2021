import json, urllib
from itertools import chain
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from MoonTrekStories.models import MoonTrekStories
from MoonTrekBlog.models import BlogPost
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MTBase.forms import ContactForm

def IndexView(request):
    return render(request, 'html/baseIndex.html')

def profileView(request, user):
    userProfile = User.objects.get(username = user)
    context = {
        'user': userProfile
    }
    return render(request, 'html/profile.html', context)

class SearchView(ListView):
    template_name = 'html/searchResults.html'
    # paginate_by = 10
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context
    
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            blog_results        = BlogPost.objects.search(query)
            stories_results     = MoonTrekStories.objects.search(query)
            character_results   = Character.objects.search(query)
            ship_results        = Ship.objects.search(query)
            places_results      = PlacesAndItems.objects.search(query)
            
            # combine querysets 
            queryset_chain = chain(
                    blog_results, 
                    stories_results, 
                    character_results, 
                    ship_results, 
                    places_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.slug, 
                        reverse=False)
            self.count = len(qs) # since qs is actually a list
            return qs
        return BlogPost.objects.none() # just an empty queryset as default

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
                ['erin@douglasavenue.com'],
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
