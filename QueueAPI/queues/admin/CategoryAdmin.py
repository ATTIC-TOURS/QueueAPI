from django.contrib import admin
from queues.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "display_name"]
    list_filter = ["branch"]

admin.site.register(Category, CategoryAdmin)