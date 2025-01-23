from django.contrib import admin
from queues.models import Window


class WindowAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Window, WindowAdmin)