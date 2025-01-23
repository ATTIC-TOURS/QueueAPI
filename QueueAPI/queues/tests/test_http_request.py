from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue, Status


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
        BRANCH_ID = 5
        url = f"{self.API_URL}/branch_login/{BRANCH_ID}"
        body =  {"password": 1234}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_categories(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/branches/{BRANCH_ID}/categories"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category(self):
        CATEGORY_ID = 1
        url = f"{self.API_URL}/categories/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/branches/{BRANCH_ID}/services"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service(self):
        SERVICE_ID = 1
        url = f"{self.API_URL}/services/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services_category(self):
        BRANCH_ID = 5
        CATEGORY_ID = 1
        url = f"{self.API_URL}/branches/{BRANCH_ID}/categories/{CATEGORY_ID}/services"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_windows(self):
        url = f"{self.API_URL}/windows"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_viewable_status(self):
        url = f"{self.API_URL}/viewable_status"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_queue(self):
        BRANCH_ID = 5
        SERVICE_ID = 1
        url = f"{self.API_URL}/queues/{BRANCH_ID}/{SERVICE_ID}"
        body =  {"queue_no": 1, "name": "cat", "is_senior_pwd": False, "pax": 12}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 5
        url = f"{self.API_URL}/queue_update/{BRANCH_ID}"
        body =  {"queue_id": 1, "status_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_queue_call(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 5
        QUEUE_ID = 1
        url = f"{self.API_URL}/queue_call/{BRANCH_ID}/{QUEUE_ID}"
        body =  {"window_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_remove_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 5
        QUEUE_ID = 1
        url = f"{self.API_URL}/remove_queue/{BRANCH_ID}/{QUEUE_ID}"
        body =  None
        response = self.client.delete(url, body)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_no_waiting(self):
        BRANCH_ID = 5
        SERVICE_ID = 1
        url = f"{self.API_URL}/branch/{BRANCH_ID}/waiting/service/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_markqueues(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/marquees/{BRANCH_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_current_queue_stats(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/branches/{BRANCH_ID}/current-queue-stats"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_controller_queues(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/branches/{BRANCH_ID}/controller-queues"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tv_now_serving(self):
        BRANCH_ID = 5
        url = f"{self.API_URL}/branches/{BRANCH_ID}/tv/now-serving"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)