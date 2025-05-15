from .constants import *


services = [
    { "name": "Tourism", "category_id": JAPAN_VISA_ID }, #1
    { "name": "Business, Conference, Cultural Exchange", "category_id": JAPAN_VISA_ID }, #2
    { "name": "Visiting Relatives", "category_id": JAPAN_VISA_ID }, #3
    { "name": "Visiting Friends", "category_id": JAPAN_VISA_ID }, #4
    { "name": "Visiting US Military Personnel", "category_id": JAPAN_VISA_ID }, #5
    { "name": "COE", "category_id": JAPAN_VISA_ID }, #6
    { "name": "Nikkei-Jin", "category_id": JAPAN_VISA_ID }, #7
    { "name": "Korea Visa", "category_id": KOREA_VISA_ID }, #8
    { "name": "China Visa", "category_id": CHINA_VISA_ID }, #9
    { "name": "International Ticket", "category_id": TICKET_ID }, #10
    { "name": "Domestic Ticket", "category_id": TICKET_ID }, #11
    { "name": "Claim Passport", "category_id": PASSPORT_ID }, #12
    { "name": "Follow Up Passport", "category_id": PASSPORT_ID }, #13
    { "name": "Tour Package", "category_id": TOUR_PACKAGE_ID }, #14
    { "name": "Data Sim Card", "category_id": OTHERS_ID }, #15
    { "name": "JR Pass", "category_id": OTHERS_ID }, #16
    { "name": "Travel Insurance", "category_id": OTHERS_ID }, #17
    { "name": "Inquire", "category_id": OTHERS_ID }, #18
]

def create_default_services(apps, schema_editor):
    Service = apps.get_model("queues", "Service")
    for service in services:
        Service.objects.create(
            name=service["name"],
            category_id=service["category_id"],
        )