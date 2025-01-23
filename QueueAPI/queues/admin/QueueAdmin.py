from django.contrib import admin
from queues.models import Queue


class QueueAdmin(admin.ModelAdmin):
    list_display = ["service", "name", "pax", "is_senior_pwd", "status", "window"]
    list_filter = ["branch", "status", "created_at"]

admin.site.register(Queue, QueueAdmin)