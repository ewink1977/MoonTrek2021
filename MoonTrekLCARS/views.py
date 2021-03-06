import random
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems

class LCARSHome(TemplateView):
    template_name = 'MoonTrekLCARS/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(LCARSHome, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Moon Trek | LCARS Database'
        # PUT THE RANDOM ARTICLE CODE HERE.

        return context

    # FUNCTION FOR FINDING A RANDOM ARTICLE TO DISPLAY!
    def randomArticle():
        fromModel = random.randint(1, 3)
        if fromModel == 1:
            last = Character.objects.all().count() - 1
            randIndex = random.randint(1, last)
            randomArticle = Character.objects.get(id = randIndex)
        if fromModel == 2:
            last = Ship.objects.all().count() - 1
            randIndex = random.randint(1, last)
            randomArticle = Ship.objects.get(id = randIndex)
        if fromModel == 3:
            last = PlacesAndItems.objects.all().count() - 1
            randIndex = random.randint(1, last)
            randomArticle = PlacesAndItems.objects.get(id = randIndex)
        return randomArticle

class Characters(ListView):
    model = Character
    ordering = ['rank']

def CharacterPartialView(request, slug):
    character = Character.objects.get(slug = slug)
    context = {
        'character': character
    }
    return render(request, 'MoonTrekLCARS/character_partial_return.html', context)

class CharacterFull(DetailView):
    model = Character

# <app>/<model>_<type>.html