from django.contrib import admin
from queues.models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Branch, BranchAdmin)