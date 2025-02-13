from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue
from queues.seeds import constants


class QueueHttpRequestTest(APITestCase):
    
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
    
    API_URL = "/queue-services/v1"
    
    def test_ptaa_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "PTAA"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_ptaa_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "PTAA"
        }
        for i in range(10):
            response = self.client.post(url, data)
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_manpower_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "MAN POWER"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_manpower_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "applicant_type": "PTAA"
        }
        for i in range(10):
            response = self.client.post(url, data)
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_inquire_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "INQUIRE"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_inquire_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "INQUIRE"
        }
        for i in range(10):
            response = self.client.post(url, data)
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_addocs_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "ADDITIONAL DOCUMENTS"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_addocs_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "ADDITIONAL DOCUMENTS"
        }
        for i in range(10):
            response = self.client.post(url, data)
            self.assertEqual(response.data["queue_no"], i+1)
    
    def test_pending_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "PENDING DOCUMENTS"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.data["queue_no"], 1)
    
    def test_multiple_pending_number(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "category": 1,
            "service": 1,
            "applicant_name": "kenji",
            "service_type": "PENDING DOCUMENTS"
        }
        for i in range(10):
            response = self.client.post(url, data)
            self.assertEqual(response.data["queue_no"], i+1)