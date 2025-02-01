from .constants import *


main_office_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": MAIN_OFFICE_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa", 
        "branch_id": MAIN_OFFICE_ID
    },
    {
        "name": "Ticket", 
        "display_name": "Ticket", 
        "branch_id": MAIN_OFFICE_ID
    },
    {
        "name": "Claim Passport", 
        "display_name": "Claim Passport", 
        "branch_id": MAIN_OFFICE_ID
    },
]

moa_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": MOA_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa", 
        "branch_id": MOA_ID
    },
    {
        "name": "Ticket", 
        "display_name": "Ticket", 
        "branch_id": MOA_ID
    },
    {
        "name": "Claim Passport", 
        "display_name": "Claim Passport", 
        "branch_id": MOA_ID
    },
]

megamall_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": MEGAMALL_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa",
        "branch_id": MEGAMALL_ID
    },
    {
        "name": "Ticket", 
        "display_name": "Ticket", 
        "branch_id": MEGAMALL_ID
    },
    {
        "name": "Claim Passport", 
        "display_name": "Claim Passport", 
        "branch_id": MEGAMALL_ID
    },
]

north_edsa_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": NORTH_EDSA_ID
    },
    {
        "name": "Korea Visa",
        "display_name": "Apply for Korea Visa",
        "branch_id": NORTH_EDSA_ID
    },
    {
        "name": "Ticket",
        "display_name": "Ticket",
        "branch_id": NORTH_EDSA_ID
    },
    {
        "name": "Claim Passport",
        "display_name": "Claim Passport", 
        "branch_id": NORTH_EDSA_ID
    },
]

fairview_categories = [
    {
        "name": "Japan Visa",
        "display_name": "Apply for Japan Visa",
        "branch_id": FAIRVIEW_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa",
        "branch_id": FAIRVIEW_ID
    },
    {
        "name": "Ticket", 
        "display_name": "Ticket", 
        "branch_id": FAIRVIEW_ID
    },
    {
        "name": "Claim Passport",
        "display_name": "Claim Passport", 
        "branch_id": FAIRVIEW_ID
    },
]

southmall_categories = [
    {
        "name": "Japan Visa",
        "display_name": "Apply for Japan Visa",
        "branch_id": SOUTHMALL_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa", 
        "branch_id": SOUTHMALL_ID
    },
    {
        "name": "Ticket",
        "display_name": "Ticket",
        "branch_id": SOUTHMALL_ID
    },
    {
        "name": "Claim Passport",
        "display_name": "Claim Passport", 
        "branch_id": SOUTHMALL_ID
    },
]

clark_categories = [
    {
        "name": "Japan Visa",
        "display_name": "Apply for Japan Visa",
        "branch_id": CLARK_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa", 
        "branch_id": CLARK_ID
    },
    {
        "name": "Ticket",
        "display_name": "Ticket",
        "branch_id": CLARK_ID
    },
    {
        "name": "Claim Passport",
        "display_name": "Claim Passport",
        "branch_id": CLARK_ID
    },
]

cebu_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": CEBU_ID
    },
    {
        "name": "Korea Visa",
        "display_name": "Apply for Korea Visa",
        "branch_id": CEBU_ID
    },
    {
        "name": "Ticket",
        "display_name": "Ticket", 
        "branch_id": CEBU_ID
    },
    {
        "name": "Claim Passport", 
        "display_name": "Claim Passport", 
        "branch_id": CEBU_ID
    },
]

davao_categories = [
    {
        "name": "Japan Visa", 
        "display_name": "Apply for Japan Visa", 
        "branch_id": DAVAO_ID
    },
    {
        "name": "Korea Visa", 
        "display_name": "Apply for Korea Visa",
        "branch_id": DAVAO_ID
    },
    {
        "name": "Ticket",
        "display_name": "Ticket", 
        "branch_id": DAVAO_ID
    },
    {
        "name": "Claim Passport",
        "display_name": "Claim Passport", 
        "branch_id": DAVAO_ID
    },
]

categories = (
    main_office_categories + 
    moa_categories +
    megamall_categories +
    north_edsa_categories +
    fairview_categories +
    southmall_categories +
    clark_categories +
    cebu_categories +
    davao_categories
)

def create_default_categories(apps, schema_editor):
    Category = apps.get_model("queues", "Category")
    for category in categories:
        Category.objects.create(
            name=category["name"],
            display_name=category["display_name"],
            branch_id=category["branch_id"]
        )