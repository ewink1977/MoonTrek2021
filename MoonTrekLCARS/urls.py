from django.urls import path
from MoonTrekLCARS import views as LCARSView

app_name = 'LCARS'

urlpatterns = [
    path('', LCARSView.LCARSHome.as_view(), name = 'lcarsHome'),
    path('characters/', LCARSView.Characters.as_view(), name = 'characterHome'),
    path('characters/p/<slug:slug>', LCARSView.CharacterPartialView, name = 'charPartialView'),
    path('characters/<slug:slug>/', LCARSView.CharacterFull.as_view(), name = 'characterView'),
    path('misc/', LCARSView.Miscellanious.as_view(), name = 'miscHome'),
    path('misc/p/<slug:slug>', LCARSView.MiscPartialView, name = 'miscPartialView'),
    path('misc/<slug:slug>/', LCARSView.MiscellaniousFull.as_view(), name = 'miscView'),
    path('ships/', LCARSView.Ships.as_view(), name = 'shipHome'),
    path('ships/p/<slug:slug>', LCARSView.ShipPartialView, name = 'shipPartialView'),
    path('ships/<slug:slug>/', LCARSView.ShipFull.as_view(), name = 'shipView'),
]