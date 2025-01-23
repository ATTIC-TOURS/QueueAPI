from .constants import *


services = [
    {"name": "Tourism", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": "Tourist Visa is only March 21 onwards accepted & (60pax/day)", "cut-off": False},
    # {"name": "Package Tour", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "Business, Conference, Cultural Exchange", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "Visiting Relatives", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "Visiting Friends", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "Visiting US Military Personnel", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Spouse/Child of a Japanese National in the Philippines", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "COE", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Transit", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Frequent Traveler", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Philippine Nationals with Considerable Financial Capacity", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Business Purpose, and Cultural or Intellectual Figures", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Student, Worker and Dependent", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Diplomat/Official", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Housekeeper hired by Diplomat/Official", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Medical Stay", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    # {"name": "Nikkei-Jin", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    
    {"name": "Korea Visa", "branch_id": FAIRVIEW_ID, "category_id": KOREA_VISA_ID, "notes": None, "cut-off": False},
    
    {"name": "International", "branch_id": FAIRVIEW_ID, "category_id": TICKET_ID, "notes": None, "cut-off": False},
    {"name": "Domestic", "branch_id": FAIRVIEW_ID, "category_id": TICKET_ID, "notes": None, "cut-off": False},
    
    
    # {"name": "Filipino Parent travelling to Japan with JFC", "branch_id": FAIRVIEW_ID, "category_id": JAPAN_VISA_ID, "notes": None, "cut-off": False},
    {"name": "Claim Passport", "branch_id": FAIRVIEW_ID, "category_id": CLAIM_PASSPORT_ID, "notes": None, "cut-off": False},
    # {"name": "Visa Consultation", "category_id": VISA_CONSULTATION_ID},
    # {"name": "Take Photograph", "category_id": ADD_ONS_ID},
    # {"name": "Photocopy Documents", "category_id": ADD_ONS_ID},
    # {"name": "Print Documents", "category_id": ADD_ONS_ID},
    # {"name": "Receive Passport via LBC", "category_id": ADD_ONS_ID},
    # {"name": "Drop-off Application", "category_id": OTHERS_ID},
    # {"name": "Submit Add Docs", "category_id": OTHERS_ID}
]

def create_default_services(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    Service = apps.get_model("queues", "Service")
    for service in services:
        Service.objects.create(
            name=service["name"],
            category_id=service["category_id"],
            notes=service["notes"],
            is_cut_off=service["cut-off"],
            branch_id=service["branch_id"]
        )