from django.contrib import admin
from .models import Fish


class FishAdmin(admin.ModelAdmin):
    list_display = ['fish_name', 'fish_value', 'fish_location']
    list_filter = ['fish_location']
    order = ['fish_name']
    exclude = ['fish_id']
    actions_on_top = False
    search_fields = ['fish_name']


admin.site.register(Fish, FishAdmin)
