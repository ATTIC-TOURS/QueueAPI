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
    
    API_URL = "/queue-services/v1"
    
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
        data = { "branch_id": constants.MAIN_OFFICE_ID }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category(self):
        CATEGORY_ID = 1
        url = f"{self.API_URL}/categories/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services(self):
        url = f"{self.API_URL}/services"
        data = { "branch_id": constants.MAIN_OFFICE_ID }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service(self):
        SERVICE_ID = 1
        url = f"{self.API_URL}/services/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services_by_category(self):
        url = f"{self.API_URL}/services"
        data = { 
                "branch_id": constants.MAIN_OFFICE_ID, 
                "category_id": constants.JAPAN_VISA_MAIN_OFFICE_ID
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_windows(self):
        url = f"{self.API_URL}/windows"
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
            "category": 1,
            "service": 1,
            # "service_type": "Additional Documents",
            # "status": 1,
            # "queue_code": "J-T1",
            "applicant_name": "Kenji",
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
        
    def test_markqueues(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/marquees/{BRANCH_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_current_queue_stats(self):
        url = f"{self.API_URL}/current-queue-stats"
        data = { "branch_id": constants.MAIN_OFFICE_ID }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_controller_queues(self):
        url = f"{self.API_URL}/controller-queues"
        data = { "branch_id": constants.MAIN_OFFICE_ID }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tv_now_serving(self):
        url = f"{self.API_URL}/tv-now-serving-queues"
        data = { "branch_id":constants.MAIN_OFFICE_ID }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)