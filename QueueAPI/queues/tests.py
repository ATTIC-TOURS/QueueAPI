from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue, Status


class HttpRequestTest(APITestCase):
    
    # Requirements
    # 1. Request
    # 2. Response
    # 3. Assertion
    
    def test_branches(self):
        url = "/branches"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_branch_login(self):
        BRANCH_ID = 1
        url = f"/branch_login/{BRANCH_ID}"
        body =  {"password": 1234}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_categories(self):
        url = "/categories"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category(self):
        CATEGORY_ID = 1
        url = f"/categories/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service_types(self):
        url = "/service_types"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service_type(self):
        CATEGORY_ID = 1
        url = f"/service_types/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services(self):
        url = "/services"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service(self):
        SERVICE_ID = 1
        url = f"/services/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services_category(self):
        CATEGORY_ID = 1
        url = f"/services/category/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_windows(self):
        url = "/windows"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_viewable_status(self):
        url = "/viewable_status"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_queue(self):
        BRANCH_ID = 1
        SERVICE_ID = 1
        url = f"/queues/{BRANCH_ID}/{SERVICE_ID}"
        body =  {"queue_no": 1, "name": "cat", "is_senior_pwd": False}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        url = f"/queue_update/{BRANCH_ID}"
        body =  {"queue_id": 1, "status_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_queue_call(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        QUEUE_ID = 1
        url = f"/queue_call/{BRANCH_ID}/{QUEUE_ID}"
        body =  {"window_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_remove_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        QUEUE_ID = 1
        url = f"/remove_queue/{BRANCH_ID}/{QUEUE_ID}"
        body =  None
        response = self.client.delete(url, body)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_no_waiting(self):
        BRANCH_ID = 1
        SERVICE_ID = 1
        url = f"/branch/{BRANCH_ID}/waiting/service/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_printer(self):
        BRANCH_ID = 1
        PRINTER_MAC_ADDRESS = "123.123.123.123"
        url = f"/printer/{BRANCH_ID}"
        body =  {"mac_address": PRINTER_MAC_ADDRESS}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_printer_status(self):
        # add first the printer
        self.test_printer()
        
        PRINTER_MAC_ADDRESS = "123.123.123.123"
        url = "/printer_status"
        body =  {"error_msg": "None", "mac_address": PRINTER_MAC_ADDRESS}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_mobile(self):
        MOBILE_MAC_ADDRESS = "123.123.123.123.123"
        url = "/mobile"
        body =  {"branch_id": 1, "mac_address": MOBILE_MAC_ADDRESS}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_mobile_status(self):
        # add first the mobile
        self.test_mobile()
        
        MOBILE_MAC_ADDRESS = "123.123.123.123.123"
        url = "/mobile_status"
        body =  {"mac_address": MOBILE_MAC_ADDRESS}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_markqueues(self):
        BRANCH_ID = 1
        url = f"/markqueues/{BRANCH_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)