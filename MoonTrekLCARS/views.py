from django.shortcuts import render
from django.template import Template, RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems
from MoonTrekLCARS.keys import charDepartment, shipFaction

class LCARSHome(TemplateView):
    template_name = 'MoonTrekLCARS/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(LCARSHome, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Moon Trek | LCARS Database'

        return context

# CHARACTERS!

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

class Miscellanious(ListView):
    model = PlacesAndItems
    ordering = ['name']

def MiscPartialView(request, slug):
    misc = PlacesAndItems.objects.get(slug = slug)
    context = {
        'misc': misc
    }
    return render(request, 'MoonTrekLCARS/misc_partial_return.html', context)

class MiscellaniousFull(DetailView):
    model = PlacesAndItems
    context_object_name = 'misc'

    def get_context_data(self, **kwargs):
        context = super(MiscellaniousFull, self).get_context_data(**kwargs)
        self.object.urlSafe = Template(
            self.object.content
        ).render(RequestContext(self.request, context))

        return context

# <app>/<model>_<type>.html