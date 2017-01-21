from django.contrib import admin
from .models import Apps

admin.site.site_title = 'Practo - One Health App'
admin.site.site_header = 'Practo - One Health App'
admin.site.disable_action('delete_selected')


@admin.register(Apps)
class AppsAdmin(admin.ModelAdmin):
    pass
