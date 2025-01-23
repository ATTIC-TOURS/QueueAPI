from django.contrib import admin
from queues.models import Marquee


class MarqueeAdmin(admin.ModelAdmin):
    list_display = ["text"]
    list_filter = ["branch"]
    
admin.site.register(Marquee, MarqueeAdmin)