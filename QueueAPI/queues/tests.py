from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class GenerateQueueTest(APITestCase):
    
    def test_generate_new_queue(self):
        """
        Ensure we can generate a new queue
        """
        url = "/queues/1/1/"
        data = {"queue_no": 1, "name": "kenji", "email": ""}
        _format = "json"
        response = self.client.post(url, data, format=_format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
