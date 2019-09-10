from django.contrib import admin
from .models import topProjects, featurette, contact

# Register your models here.

class chng(admin.ModelAdmin):
    list_display=('title',)

admin.site.site_header = 'Kama Systems'
admin.site.site_title = 'KamaSystems'
admin.site.register(topProjects, chng)
admin.site.register(featurette)
admin.site.register(contact)
