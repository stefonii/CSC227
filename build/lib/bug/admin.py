from django.contrib import admin
from . models import Bug


class BugAdmin(admin.ModelAdmin):
    list_display = ['bug_name', 'bug_value']
    list_filter = ['bug_value']
    order = ['bug_name']
    exclude = ['bug_id']
    actions_on_top = False
    search_fields = ['bug_name']


admin.site.register(Bug, BugAdmin)
