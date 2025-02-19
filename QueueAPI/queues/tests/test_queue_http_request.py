from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Queue, Status
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
    
    # Requirements
    # 1. Request
    # 2. Response
    # 3. Assertion
    
    API_URL = "/queue-services/v1"
    
    def setUp(self):
        queue = Queue.objects.create(
            branch_id=constants.MAIN_OFFICE_ID,
            category_id=constants.JAPAN_VISA_MAIN_OFFICE_ID,
            service_id=1,
            applicant_name="Kenji",
            no_applicant=5
        )
        self.queue_id = queue.id
    
    def test_get_queue(self):
        url = f"{self.API_URL}/queues/{self.queue_id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_queue(self):
        url = f"{self.API_URL}/queues/{self.queue_id}"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_change_no_applicant(self):
        url = f"{self.API_URL}/queues/{self.queue_id}"
        data = {"no_applicant": 5}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_change_status(self):
        url = f"{self.API_URL}/queues/{self.queue_id}"
        data = {"status": 1}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_call_queue(self):
        url = f"{self.API_URL}/queues/{self.queue_id}"
        data = {"is_called": True, "window": 1}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_branch_queues(self):
        url = f"{self.API_URL}/queues"
        data = {"branch_id": constants.MAIN_OFFICE_ID}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_all_queues(self):
        url = f"{self.API_URL}/queues"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)