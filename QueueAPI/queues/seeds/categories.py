from .constants import *


categories = [
    {"name": "Japan Visa", "display_name": "Apply for Japan Visa", "branch_id": FAIRVIEW_ID},
    {"name": "Korea Visa", "display_name": "Apply for Korea Visa", "branch_id": FAIRVIEW_ID},
    {"name": "Ticket", "display_name": "Ticket", "branch_id": FAIRVIEW_ID},
    {"name": "Claim Passport", "display_name": "Claim Passport", "branch_id": FAIRVIEW_ID},
    # {"name": "Visa Consultation", "display_name": "Visa Consultation"},
    # {"name": "Add ons", "display_name": "Add ons"},
    # {"name": "Others", "display_name": "Others"}
]

def create_default_categories(apps, schema_editor):
    Category = apps.get_model("queues", "Category")
    for category in categories:
        Category.objects.create(
            name=category["name"],
            display_name=category["display_name"],
            branch_id=category["branch_id"]
        )