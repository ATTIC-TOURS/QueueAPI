from .constants import *


marquees = [
    {"branch_id": MAIN_OFFICE_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MAIN_OFFICE_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": MOA_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MOA_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": NORTH_EDSA_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": NORTH_EDSA_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": MEGAMALL_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MEGAMALL_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": FAIRVIEW_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": FAIRVIEW_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": FAIRVIEW_ID, "text": "Due to the rapid increase in the number of visitors from the Philippines, examination of visa applications for tourism purposes, may take several weeks longer than the standard processing time. Therefore, we highly recommend for applicants to please apply at least two months prior to the date of travel."},
    {"branch_id": SOUTHMALL_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": SOUTHMALL_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": CLARK_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": CLARK_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": CEBU_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": CEBU_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": DAVAO_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": DAVAO_ID, "text": "Please issue a queue and wait for to be called!"},
]


def create_default_marquees(apps, schema_editor):
    Branch = apps.get_model("queues", "Branch")
    Marquee = apps.get_model("queues", "Marquee")
    for marquee in marquees:
        Marquee.objects.create(
            branch=Branch.objects.get(id=marquee["branch_id"]),
            text=marquee["text"]
        )