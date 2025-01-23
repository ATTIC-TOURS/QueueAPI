from django.contrib import admin
from queues.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "notes", "branch", "quota", "is_cut_off"]
    list_filter = ["branch", "is_cut_off"]

admin.site.register(Service, ServiceAdmin)