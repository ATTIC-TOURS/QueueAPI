from django.contrib import admin
from queues.models import Service, Window, Branch, Status, Queue, Mobile, Printer, MarkQueue


admin.site.register(Service)
admin.site.register(Window)
admin.site.register(Branch)
admin.site.register(Status)
admin.site.register(Queue)
admin.site.register(Mobile)
admin.site.register(Printer)
admin.site.register(MarkQueue)