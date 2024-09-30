from django.contrib import admin
from .models import Tag, Site_tag

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('id_tag', 'tag')
    list_filter = ('tag',)

    fieldsets = (
        (None, {
            'fields': ('tag',)
        }),
    )

class Site_tagAdmin(admin.ModelAdmin):
    model = Site_tag
    list_display = ('id_site_tag', 'site_tour', 'tag')
    list_filter = ('site_tour', 'tag')

    fieldsets = (
        (None, {
            'fields': ('site_tour', 'tag')
        }),
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(Site_tag, Site_tagAdmin)