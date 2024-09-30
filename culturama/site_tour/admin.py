from django.contrib import admin
from .models import Site_tour

# Register your models here.

class SitesAdmin(admin.ModelAdmin):
    model = Site_tour
    list_display = ['site_name', 'description', 'url', 'image', 'adress', 'coordinates', 'journey_time', 'site_type', 'accesibility', 'state']
    list_filter = ['site_type', 'state']

    fieldsets = (
        (None, {
            'fields': ('site_name', 'url', 'image')
        }),
        ('Información', {
            'fields': ('description','adress', 'coordinates', 'journey_time', 'site_type', 'accesibility')
        }),
        ('Acciones', {
            'fields': ('state',)
        }),
    )

admin.site.register(Site_tour, SitesAdmin)