import random
from django.db import models
from django.shortcuts import render, redirect
from django.template import Template, RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MoonTrekLCARS.keys import charFaction, charRank, charDepartment, shipFaction


class LCARSHome(TemplateView):
    template_name = 'MoonTrekLCARS/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(LCARSHome, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Moon Trek | LCARS Database'

        return context

# CHARACTERS!

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

# SHIPS!

class Ships(ListView):
    model = Ship
    ordering = ['faction']

def ShipPartialView(request, slug):
    ship = Ship.objects.get(slug = slug)
    context = {
        'ship': ship
    }
    return render(request, 'MoonTrekLCARS/ship_partial_return.html', context)

class ShipFull(DetailView):
    model = Ship
    context_object_name = 'ship'

    def get_context_data(self, **kwargs):
        context = super(ShipFull, self).get_context_data(**kwargs)
        context['factionDict'] = shipFaction
        self.object.urlSafe = Template(
            self.object.content
        ).render(RequestContext(self.request, context))

        return context

# <app>/<model>_<type>.html