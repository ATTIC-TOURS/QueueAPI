from .constants import *


marquees = [
    {"branch_id": MAIN_OFFICE_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MAIN_OFFICE_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": MOA_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MOA_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": MEGAMALL_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": MEGAMALL_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": NORTH_EDSA_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": NORTH_EDSA_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": FAIRVIEW_ID, "text": "Welcome to Attic Tours!"},
    {"branch_id": FAIRVIEW_ID, "text": "Please issue a queue and wait for to be called!"},
    {"branch_id": FAIRVIEW_ID, "text": "Your turn might be skipped for assessing applications for Senior/PWD"},
    {"branch_id": FAIRVIEW_ID, "text": "Due to the rapid increase in the number of visitors from the Philippines, examination of visa applications for tourism purposes, may take several weeks longer than the standard processing time. Therefore, we highly recommend for applicants to please apply at least two months prior to the date of travel."},
    {"branch_id": FAIRVIEW_ID, "text": "Starting JANUARY 19, 2025, ATTIC TOURS will only be accepting new applications for Japan Tourist Visa with travel dates of MARCH 21, 2025 onwards."},
    {"branch_id": FAIRVIEW_ID, "text": "All those with travel dates prior to March 15, 2025 WILL NOT BE ACCEPTED ANYMORE, even if the applicant is willing to sign a waiver."},
    {"branch_id": FAIRVIEW_ID, "text": "Furthermore, ATTIC TOURS will only be accepting 60 pax a day."},
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