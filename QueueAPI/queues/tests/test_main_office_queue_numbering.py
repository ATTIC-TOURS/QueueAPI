from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue
from queues.seeds import constants


class MainOfficeQueueNumberTest(APITestCase):
    
    # data = {
    #         "branch": constants.MAIN_OFFICE_ID,
    #         "category": 1,
    #         "service": 1,
    #         # "service_type": "Additional Documents",
    #         # "status": 1,
    #         # "queue_code": "J-T1",
    #         "applicant_name": "Kenji",
    #         # "no_applicant": 5,
    #         # "applicant_type": "Walk-In",
    #         # "is_senior_pwd": True,
    #         # "queue_no": 1,
    #         # "coordinator_name": "Hazel",
    #         # "is_called": False,
    #         # "is_priority": True
    #     }
    
    endpoint = "/api/queues/v2/queues"
    data = {
        "PTAA": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "PTAA",
            "no_applicant": 5
        },
        "MAN POWER": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "MAN POWER",
            "no_applicant": 5
        },
        "INQUIRE": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "INQUIRE",
            "no_applicant": 5
        },
        "ADDOCS": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "ADDITIONAL DOCUMENTS",
            "no_applicant": 5
        },
        "PENDING": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "PENDING DOCUMENTS",
            "no_applicant": 5
        },
        "WALK-IN": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "WALK-IN",
            "no_applicant": 5
        },
        "TA": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "NON PTAA",
            "no_applicant": 5
        },
        "TICKET": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": constants.TICKET_MAIN_OFFICE_ID,
            "service": 8, # temp static number
            "applicant_name": "kenji",
            "no_applicant": 5
        },
        "PASSPORT": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": constants.PASSPORT_MAIN_OFFICE_ID,
            "service": 10, # temp static number
            "applicant_name": "kenji",
            "no_applicant": 5
        }
    }
    
    def test_ptaa_number(self):
        response = self.client.post(self.endpoint, self.data["PTAA"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_ptaa_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["PTAA"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_manpower_number(self):
        response = self.client.post(self.endpoint, self.data["MAN POWER"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_manpower_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["MAN POWER"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_inquire_number(self):
        response = self.client.post(self.endpoint, self.data["INQUIRE"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_inquire_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["INQUIRE"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_addocs_number(self):
        response = self.client.post(self.endpoint, self.data["ADDOCS"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_addocs_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["ADDOCS"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_pending_number(self):
        response = self.client.post(self.endpoint, self.data["PENDING"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_pending_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["PENDING"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_walkin_number(self):
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_walkin_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["WALK-IN"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_ta_number(self):
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_ta_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["TA"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_ticket_number(self):
        response = self.client.post(self.endpoint, self.data["TICKET"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_ticket_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["TICKET"])
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_passport_number(self):
        response = self.client.post(self.endpoint, self.data["PASSPORT"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_passport_number(self):
        for i in range(10):
            response = self.client.post(self.endpoint, self.data["PASSPORT"])
            self.assertEqual(response.data["queue_no"], i+1)