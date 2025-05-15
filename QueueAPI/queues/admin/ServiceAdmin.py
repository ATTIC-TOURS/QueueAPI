from django.contrib import admin
from queues.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]

admin.site.register(Service, ServiceAdmin)