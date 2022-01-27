from django.contrib import admin
from .models import Counters  

# Register your models here.

admin.site.register(Counters)

admin.site.site_header = 'EYC Site Administration | لوحة تحكم موقع مجلس الشباب المصري'
admin.site.site_title  = 'EYC Site Administration'


