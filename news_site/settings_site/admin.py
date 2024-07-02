from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 
from django.contrib.auth.models import Permission
from .models import * 


# @admin.register(Settings)
# class SettingsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ['name_site']
#     search_fields = ['name_site']
#     autocomplete_fields = ['tab_name','telegram_url','instagram_url','whatsapp_url','email','copy_right','number','logo_favicon','logo_header','logo_header_menu','logo_footer','site_title','about_us','address']
#     list_filter = []
#     ordering = ["-id"]
#     readonly_fields = []
#     prepopulated_fields = {}
#     # date_hierarchy = 'created_at'
#     empty_value_display = '-'


admin.site.register(Permission)
admin.site.register(Settings)
admin.site.register(ContactUsSettings)
admin.site.register(ContactUs)

