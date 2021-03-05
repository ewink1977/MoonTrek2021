from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems

def buffer(request):
    return render(request, 'html/baseIndex.html')

class LCARSHome(ListView):
    context_object_name = 'character_list'
    model = Character
    template_name = 'MoonTrekLCARS/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(LCARSHome, self).get_context_data(**kwargs)
        context['ship_list'] = Ship.objects.all()
        context['place_item_list'] = PlacesAndItems.objects.all()
        context['pagetitle'] = 'Moon Trek | LCARS Database'

        return context


# <app>/<model>_<type>.html