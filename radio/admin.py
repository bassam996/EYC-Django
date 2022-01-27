from django.contrib import admin
from .models import All_Season , Episodes

# Register your models here.

class EpisodesAdmin(admin.ModelAdmin):
    list_display       = [  'episode_name' , 'episode_name_en'  ,'episode_url' , 'link' ]
    list_display_links = ['episode_name' , 'episode_name_en']
    list_editable      = [  'episode_url', 'link']
    list_filter        = ['link']


admin.site.register(All_Season)
admin.site.register(Episodes , EpisodesAdmin)
