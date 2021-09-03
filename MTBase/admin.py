from django.contrib import admin
from .models import Profile, LandingAlert

class AlertAdmin(admin.ModelAdmin):
    list_display = ('alertText', 'alertType', 'created_at')

admin.site.register(Profile)
admin.site.register(LandingAlert, AlertAdmin)


