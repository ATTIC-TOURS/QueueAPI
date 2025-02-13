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
    
    endpoint = "/queue-services/v1/queues"
    data = {
        "PTAA": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "PTAA"
        },
        "MAN POWER": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "MAN POWER"
        },
        "INQUIRE": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "INQUIRE"
        },
        "ADDOCS": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "ADDITIONAL DOCUMENTS"
        },
        "PENDING": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "PENDING DOCUMENTS"
        },
        "WALK-IN": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "WALK-IN",
        },
        "TA": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "TRAVEL AGENCY",
        },
        "TICKET": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": constants.TICKET_MAIN_OFFICE_ID,
            "service": 8, # temp static number
            "applicant_name": "kenji",
        },
        "PASSPORT": {
            "branch": constants.MAIN_OFFICE_ID,
            "category": constants.PASSPORT_MAIN_OFFICE_ID,
            "service": 10, # temp static number
            "applicant_name": "kenji",
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
    
    def test_walkin_and_ta_number(self):
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_walkin_and_ta_and_walkin_number(self):
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 2)
    
    def test_all_at_the_same_time_number(self):
        # PTAA
        response = self.client.post(self.endpoint, self.data["PTAA"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # MAN POWER
        response = self.client.post(self.endpoint, self.data["MAN POWER"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # INQUIRE
        response = self.client.post(self.endpoint, self.data["INQUIRE"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # ADDOCS
        response = self.client.post(self.endpoint, self.data["ADDOCS"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # PENDING
        response = self.client.post(self.endpoint, self.data["PENDING"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TICKET
        response = self.client.post(self.endpoint, self.data["TICKET"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # PASSPORT
        response = self.client.post(self.endpoint, self.data["PASSPORT"])
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_all_at_the_same_time_and_multiple_times_number(self):
        # PTAA
        response = self.client.post(self.endpoint, self.data["PTAA"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # MAN POWER
        response = self.client.post(self.endpoint, self.data["MAN POWER"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # INQUIRE
        response = self.client.post(self.endpoint, self.data["INQUIRE"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # ADDOCS
        response = self.client.post(self.endpoint, self.data["ADDOCS"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # PENDING
        response = self.client.post(self.endpoint, self.data["PENDING"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TICKET
        response = self.client.post(self.endpoint, self.data["TICKET"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # PASSPORT
        response = self.client.post(self.endpoint, self.data["PASSPORT"])
        self.assertEqual(response.data["queue_no"], 1)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 2)
        
        # TICKET
        response = self.client.post(self.endpoint, self.data["TICKET"])
        self.assertEqual(response.data["queue_no"], 2)
        
        # PENDING
        response = self.client.post(self.endpoint, self.data["PENDING"])
        self.assertEqual(response.data["queue_no"], 2)
        
        # WALK-IN
        response = self.client.post(self.endpoint, self.data["WALK-IN"])
        self.assertEqual(response.data["queue_no"], 2)
        
        # TA
        response = self.client.post(self.endpoint, self.data["TA"])
        self.assertEqual(response.data["queue_no"], 3)