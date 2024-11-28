from django.contrib import admin
from queues.models import Category, Service, ServiceType, Window, Branch, Status, Queue, Mobile, Printer, MarkQueue


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["category_id", "name", "service_type_id"]
    list_filter = ["category_id", "service_type_id"]
        

class QueueAdmin(admin.ModelAdmin):
    list_filter = ["branch_id", "created_at"]


class MarkQueueAdmin(admin.ModelAdmin):
    list_filter = ["branch_id"]


admin.site.register(Category)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType)
admin.site.register(Window)
admin.site.register(Branch)
admin.site.register(Queue, QueueAdmin)
admin.site.register(Mobile)
admin.site.register(Printer)
admin.site.register(MarkQueue, MarkQueueAdmin)