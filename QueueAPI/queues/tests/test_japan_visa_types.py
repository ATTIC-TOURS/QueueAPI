from rest_framework import status
from rest_framework.test import APITestCase
from queues.models import Service
from queues.seeds import constants


class JapanVisaTypesTest(APITestCase):
    
    def test_japan_visa_type_list(self):
        endpoint = "/queue-services/v1/japan-visa-types"
        data = { "branch_id": constants.MAIN_OFFICE_ID }
        response = self.client.get(endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_japan_visa_type_detail(self):
        endpoint = "/queue-services/v1/japan-visa-types/1"
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_change_quota(self):
        endpoint = "/queue-services/v1/japan-visa-types/1"
        data = { "quota": 50 }
        response = self.client.patch(endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_change_notes(self):
        endpoint = "/queue-services/v1/japan-visa-types/1"
        data = { "notes": "as of now cut off" }
        response = self.client.patch(endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)