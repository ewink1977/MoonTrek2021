import random
from django.db import models
from django.shortcuts import render, redirect
from django.template import Template, RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MoonTrekLCARS.keys import charFaction, charRank, charDepartment

# FUNCTION FOR FINDING A RANDOM ARTICLE TO DISPLAY!
def randomArticle():
        fromModel = random.randint(1, 3)
        if fromModel == 1:
            last = Character.objects.all().count()
            randIndex = random.randint(1, last)
            randomArticle = Character.objects.get(id = randIndex)
        if fromModel == 2:
            last = Ship.objects.all().count()
            randIndex = random.randint(1, last)
            randomArticle = Ship.objects.get(id = randIndex)
        if fromModel == 3:
            last = PlacesAndItems.objects.all().count()
            randIndex = random.randint(1, last)
            randomArticle = PlacesAndItems.objects.get(id = randIndex)
        return randomArticle

class LCARSHome(TemplateView):
    template_name = 'MoonTrekLCARS/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(LCARSHome, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Moon Trek | LCARS Database'

        return context

class Characters(ListView):
    model = Character
    ordering = ['name']

def CharacterPartialView(request, slug):
    character = Character.objects.get(slug = slug)
    context = {
        'character': character
    }
    return render(request, 'MoonTrekLCARS/character_partial_return.html', context)

class CharacterFull(DetailView):
    model = Character
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        context = super(CharacterFull, self).get_context_data(**kwargs)
        context['deptDict'] = charDepartment
        self.object.urlSafe = Template(
            self.object.content
        ).render(RequestContext(self.request, context))

        return context

# <app>/<model>_<type>.html