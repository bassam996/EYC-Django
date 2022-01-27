from django.contrib import admin
from .models import Board , Branches , Volunteering , Switch_V_Form , Contact , Partnerships
from import_export.admin import ImportExportModelAdmin

@admin.register(Volunteering)
class VolImportExport(ImportExportModelAdmin):
    pass

# Register your models here.

admin.site.register(Board)
admin.site.register(Branches)
admin.site.register(Switch_V_Form)
admin.site.register(Contact)
admin.site.register(Partnerships)
