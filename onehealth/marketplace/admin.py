from django.contrib import admin
from .models import Apps

admin.site.site_title = 'One Health Apps'
admin.site.site_header = 'One Health Apps'


@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    pass
