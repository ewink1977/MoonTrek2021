from django.urls import path
from MoonTrekLCARS import views as LCARSView

app_name = 'LCARS'

urlpatterns = [
    path('', LCARSView.LCARSHome.as_view(), name = 'lcarsHome'),
    path('Characters/', LCARSView.Characters.as_view(), name = 'characterHome'),
    path('Characters/p/<slug:slug>', LCARSView.CharacterPartialView, name = 'charPartialView'),
    path('Characters/<slug:slug>/', LCARSView.CharacterFull.as_view(), name = 'characterView'),
    path('Ships/', LCARSView.Ships.as_view(), name = 'shipHome'),
    path('Ships/p/<slug:slug>', LCARSView.ShipPartialView, name = 'shipPartialView'),
    path('Ships/<slug:slug>/', LCARSView.ShipFull.as_view(), name = 'shipView'),
]