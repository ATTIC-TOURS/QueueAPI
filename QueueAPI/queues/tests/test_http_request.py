from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue, Status
from queues.seeds import constants


class HttpRequestTest(APITestCase):
    
    # Requirements
    # 1. Request
    # 2. Response
    # 3. Assertion
    
    API_URL = "/api/queues/v2"
    
    def test_branches(self):
        url = f"{self.API_URL}/branches"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_branch_login(self):
        url = f"{self.API_URL}/branch_login"
        data =  { "branch_id": constants.MAIN_OFFICE_ID, "password": "mainoffice"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_categories(self):
        url = f"{self.API_URL}/categories"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services(self):
        url = f"{self.API_URL}/services"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_statuses(self):
        url = f"{self.API_URL}/statuses"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_new_add_queue(self):
        url = f"{self.API_URL}/queues"
        data = {
            "branch": constants.MAIN_OFFICE_ID,
            "service": 1,
            # "service_type": "Additional Documents",
            # "status": 1,
            # "queue_code": "J-T1",
            "applicant_name": "Kenji",
            "no_applicant": 5
            # "no_applicant": 5,
            # "applicant_type": "Walk-In",
            # "is_senior_pwd": True,
            # "queue_no": 1,
            # "coordinator_name": "Hazel",
            # "is_called": False,
            # "is_priority": True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)