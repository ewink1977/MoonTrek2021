from django.contrib import admin
from MoonTrekLCARS.models import Character, Ship, PlacesAndItems

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')

class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'faction')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'slug')

admin.site.register(Character, CharacterAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(PlacesAndItems, PlaceAdmin)