from .constants import *


categories = [
    { "name": JAPAN_VISA, },
    { "name": KOREA_VISA, },
    { "name": CHINA_VISA, },
    { "name": TICKET, },
    { "name": PASSPORT, },
    { "name": TOUR_PACKAGE, },
    { "name": OTHER_VISA, },
    { "name": OTHERS, },
]

def create_default_categories(apps, schema_editor):
    Category = apps.get_model("queues", "Category")
    for category in categories:
        Category.objects.create(
            name=category["name"],
        )