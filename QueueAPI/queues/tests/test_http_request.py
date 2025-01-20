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
        url = "/queue-services/v1/branches"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_branch_login(self):
        BRANCH_ID = 1
        url = f"/queue-services/v1/branch_login/{BRANCH_ID}"
        body =  {"password": 1234}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_categories(self):
        url = "/queue-services/v1/categories"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_category(self):
        CATEGORY_ID = 1
        url = f"/queue-services/v1/categories/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service_types(self):
        url = "/queue-services/v1/service_types"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service_type(self):
        CATEGORY_ID = 1
        url = f"/queue-services/v1/service_types/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services(self):
        url = "/queue-services/v1/services"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_service(self):
        SERVICE_ID = 1
        url = f"/queue-services/v1/services/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_services_category(self):
        CATEGORY_ID = 1
        url = f"/queue-services/v1/services/category/{CATEGORY_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_windows(self):
        url = "/queue-services/v1/windows"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_viewable_status(self):
        url = "/queue-services/v1/viewable_status"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_add_queue(self):
        BRANCH_ID = 1
        SERVICE_ID = 1
        url = f"/queue-services/v1/queues/{BRANCH_ID}/{SERVICE_ID}"
        body =  {"queue_no": 1, "name": "cat", "is_senior_pwd": False, "pax": 12}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        url = f"/queue-services/v1/queue_update/{BRANCH_ID}"
        body =  {"queue_id": 1, "status_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_queue_call(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        QUEUE_ID = 1
        url = f"/queue-services/v1/queue_call/{BRANCH_ID}/{QUEUE_ID}"
        body =  {"window_id": 1}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_remove_queue(self):
        # add first the queue
        self.test_add_queue()
        
        BRANCH_ID = 1
        QUEUE_ID = 1
        url = f"/queue-services/v1/remove_queue/{BRANCH_ID}/{QUEUE_ID}"
        body =  None
        response = self.client.delete(url, body)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_no_waiting(self):
        BRANCH_ID = 1
        SERVICE_ID = 1
        url = f"/queue-services/v1/branch/{BRANCH_ID}/waiting/service/{SERVICE_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_printer(self):
        BRANCH_ID = 1
        PRINTER_MAC_ADDRESS = "123.123.123.123"
        url = f"/queue-services/v1/printer/{BRANCH_ID}"
        body =  {"mac_address": PRINTER_MAC_ADDRESS}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_printer_status(self):
        # add first the printer
        self.test_printer()
        
        PRINTER_MAC_ADDRESS = "123.123.123.123"
        url = "/queue-services/v1/printer_status"
        body =  {"error_msg": "None", "mac_address": PRINTER_MAC_ADDRESS}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_mobile(self):
        MOBILE_MAC_ADDRESS = "123.123.123.123.123"
        url = "/queue-services/v1/mobile"
        body =  {"branch_id": 1, "mac_address": MOBILE_MAC_ADDRESS}
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_mobile_status(self):
        # add first the mobile
        self.test_mobile()
        
        MOBILE_MAC_ADDRESS = "123.123.123.123.123"
        url = "/queue-services/v1/mobile_status"
        body =  {"mac_address": MOBILE_MAC_ADDRESS}
        response = self.client.patch(url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_markqueues(self):
        BRANCH_ID = 1
        url = f"/queue-services/v1/markqueues/{BRANCH_ID}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_current_queue_stats(self):
        BRANCH_ID = 1
        url = f"/queue-services/v1/branches/{BRANCH_ID}/current-queue-stats"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_controller_queues(self):
        BRANCH_ID = 1
        url = f"/queue-services/v1/branches/{BRANCH_ID}/controller-queues"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_tv_now_serving(self):
        BRANCH_ID = 1
        url = f"/queue-services/v1/branches/{BRANCH_ID}/tv/now-serving"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)