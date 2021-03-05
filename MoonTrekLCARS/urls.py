from django.urls import path
from MoonTrekLCARS import views as LCARSView

app_name = 'LCARS'

urlpatterns = [
    path('', LCARSView.LCARSHome.as_view(), name = 'lcarsHome'),
]