from django.contrib import admin
from queues.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Category, CategoryAdmin)