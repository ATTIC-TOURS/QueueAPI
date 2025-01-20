branches = [
    {"name": "Main Office", "password": "1234"},
    {"name": "SM Mall of Asia", "password": "1234"},
    {"name": "SM Megamall", "password": "1234"},
    {"name": "SM North Edsa", "password": "1234"},
    {"name": "SM Fairview", "password": "arviepogi"},
    {"name": "SM Southmall", "password": "1234"},
    {"name": "SM Clark", "password": "1234"},
    {"name": "SM Cebu", "password": "1234"},
    {"name": "SM Davao", "password": "1234"},
]

categories = [
    {"name": "Japan Visa", "display_name": "Apply for Japan Visa"},
    {"name": "Korea Visa", "display_name": "Apply for Korea Visa"},
    {"name": "Ticket", "display_name": "Ticket"},
    {"name": "Claim Passport", "display_name": "Claim Passport"},
    # {"name": "Visa Consultation", "display_name": "Visa Consultation"},
    # {"name": "Add ons", "display_name": "Add ons"},
    # {"name": "Others", "display_name": "Others"}
]

JAPAN_VISA_ID = 1
KOREA_VISA_ID = 2
TICKET_ID = 3
CLAIM_PASSPORT_ID = 4
# VISA_CONSULTATION_ID = 5
# ADD_ONS_ID = 6
# OTHERS_ID = 7

service_types = [
    {"name": "Temporary Visitor", "category_id": JAPAN_VISA_ID},
    {"name": "Multiple-Entry", "category_id": JAPAN_VISA_ID},
    {"name": "Long Term Stay", "category_id": JAPAN_VISA_ID}
]

TEMPORARY_VISITOR_ID = 1
MULTIPLE_ENTRY_ID = 2
LONG_TERM_STAY_ID = 3

services = [
    {"name": "Tourism", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": "Tourist Visa is only March 15 onwards accepted & (60pax/day)", "cut-off": False},
    {"name": "Package Tour", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Business, Conference, Cultural Exchange", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Visiting Relatives", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Visiting Friends", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Visiting US Military Personnel", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Spouse/Child of a Japanese National in the Philippines", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Transit", "category_id": JAPAN_VISA_ID, "service_type_id": TEMPORARY_VISITOR_ID, "notes": None, "cut-off": False},
    {"name": "Frequent Traveler", "category_id": JAPAN_VISA_ID, "service_type_id": MULTIPLE_ENTRY_ID, "notes": None, "cut-off": False},
    {"name": "Philippine Nationals with Considerable Financial Capacity", "category_id": JAPAN_VISA_ID, "service_type_id": MULTIPLE_ENTRY_ID, "notes": None, "cut-off": False},
    {"name": "Business Purpose, and Cultural or Intellectual Figures", "category_id": JAPAN_VISA_ID, "service_type_id": MULTIPLE_ENTRY_ID, "notes": None, "cut-off": False},
    {"name": "Student, Worker and Dependent", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    {"name": "Diplomat/Official", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    {"name": "Housekeeper hired by Diplomat/Official", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    {"name": "Medical Stay", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    {"name": "Nikkei-Jin", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    
    {"name": "Korea Visa", "category_id": KOREA_VISA_ID, "service_type_id": None, "notes": None, "cut-off": False},
    
    {"name": "International", "category_id": TICKET_ID, "service_type_id": None, "notes": None, "cut-off": False},
    {"name": "Domestic", "category_id": TICKET_ID, "service_type_id": None, "notes": None, "cut-off": False},
    
    
    {"name": "Filipino Parent travelling to Japan with JFC", "category_id": JAPAN_VISA_ID, "service_type_id": LONG_TERM_STAY_ID, "notes": None, "cut-off": False},
    {"name": "Claim Passport", "category_id": CLAIM_PASSPORT_ID, "service_type_id": None, "notes": None, "cut-off": False},
    # {"name": "Visa Consultation", "category_id": VISA_CONSULTATION_ID, "service_type_id": None},
    # {"name": "Take Photograph", "category_id": ADD_ONS_ID, "service_type_id": None},
    # {"name": "Photocopy Documents", "category_id": ADD_ONS_ID, "service_type_id": None},
    # {"name": "Print Documents", "category_id": ADD_ONS_ID, "service_type_id": None},
    # {"name": "Receive Passport via LBC", "category_id": ADD_ONS_ID, "service_type_id": None},
    # {"name": "Drop-off Application", "category_id": OTHERS_ID, "service_type_id": None},
    # {"name": "Submit Add Docs", "category_id": OTHERS_ID, "service_type_id": None}
]

windows = [
    {"name": "1"},
    {"name": "2"},
    {"name": "3"},
    {"name": "4"},
    {"name": "5"},
    {"name": "6"},
    {"name": "7"},
    {"name": "Japan Visa"},
    {"name": "Korea Visa"},
    {"name": "Ticketing"},
    {"name": "Cashier"},
]

statuses = [
    {"name": "complete"},
    {"name": "pending"},
    {"name": "waiting"},
    {"name": "in-progress"},
    {"name": "cancel"},
]

mark_queues = [
    {"branch_id": 1, "text": "Welcome to Attic Tours!"},
    {"branch_id": 1, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 2, "text": "Welcome to Attic Tours!"},
    {"branch_id": 2, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 3, "text": "Welcome to Attic Tours!"},
    {"branch_id": 3, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 4, "text": "Welcome to Attic Tours!"},
    {"branch_id": 4, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 5, "text": "Welcome to Attic Tours!"},
    {"branch_id": 5, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 5, "text": "Your turn might be skipped for assessing applications for Senior/PWD"},
    {"branch_id": 5, "text": "Due to the rapid increase in the number of visitors from the Philippines, examination of visa applications for tourism purposes, may take several weeks longer than the standard processing time. Therefore, we highly recommend for applicants to please apply at least two months prior to the date of travel."},
    {"branch_id": 5, "text": "Starting JANUARY 19, 2025, ATTIC TOURS will only be accepting new applications for Japan Tourist Visa with travel dates of MARCH 15, 2025 onwards."},
    {"branch_id": 5, "text": "All those with travel dates prior to March 15, 2025 WILL NOT BE ACCEPTED ANYMORE, even if the applicant is willing to sign a waiver."},
    {"branch_id": 5, "text": "Furthermore, ATTIC TOURS will only be accepting 60 pax a day."},
    {"branch_id": 6, "text": "Welcome to Attic Tours!"},
    {"branch_id": 6, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 7, "text": "Welcome to Attic Tours!"},
    {"branch_id": 7, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 8, "text": "Welcome to Attic Tours!"},
    {"branch_id": 8, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": 9, "text": "Welcome to Attic Tours!"},
    {"branch_id": 9, "text": "Please issue a queue and wait for to be called!"},
]


def create_default_data(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Branch = apps.get_model("queues", "Branch")
    for branch in branches:
        Branch.objects.create(
            name=branch["name"],
            password=branch["password"]
        )
    
    Category = apps.get_model("queues", "Category")
    for category in categories:
        Category.objects.create(
            name=category["name"],
            display_name=category["display_name"],
        )
    
    ServiceType = apps.get_model("queues", "ServiceType")
    for service_type in service_types:
        ServiceType.objects.create(
            name=service_type["name"],
            category_id=service_type["category_id"],
        )
    
    Service = apps.get_model("queues", "Service")
    for service in services:
        Service.objects.create(
            name=service["name"],
            category_id=service["category_id"],
            service_type_id=service["service_type_id"],
            notes=service["notes"],
            is_cut_off=service["cut-off"]
        )
    
    Window = apps.get_model("queues", "Window")
    for window in windows:
        Window.objects.create(
            name=window["name"],
        )
    
    Status = apps.get_model("queues", "Status")
    for status in statuses:
        Status.objects.create(
            name=status["name"],
        )
    
    MarkQueue = apps.get_model("queues", "MarkQueue")
    for mark_queue in mark_queues:
        MarkQueue.objects.create(
            branch=Branch.objects.get(id=mark_queue["branch_id"]),
            text=mark_queue["text"]
        )

# ADD THE FOLLOWING TO THE MIGRATIONS use python manage.py makemigrations --empty yourappname

# Generated by Django 5.1.1 on 2024-10-15 06:46

# from django.db import migrations
# from queues.seed import create_default_data

# class Migration(migrations.Migration):

#     dependencies = [
#         ("queues", "0001_initial"),
#     ]

#     operations = [migrations.RunPython(create_default_data)]