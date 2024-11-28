from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from queues.models import Queue, Status

# Create your tests here.
class GenerateQueueTest(APITestCase):
    
    def test_generate_new_queue(self):
        """
        Ensure we can generate a new queue
        """
        url = "/queues/1/1/"
        data = {"queue_no": 1, "name": "kenji", "email": "", "is_senior_pwd": False}
        _format = "json"
        response = self.client.post(url, data, format=_format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DeleteQueueTest(APITestCase):
    
    def test_delete_queue(self):
        """
        Ensure we can delete a queue after generating a new queue
        """
        branch_id = 1
        url = f"/queues/{branch_id}/1/"
        data = {"queue_no": 1, "name": "kenji", "email": "", "is_senior_pwd": True}
        _format = "json"
        response = self.client.post(url, data, format=_format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        queue = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        ).first()
        
        url = f"/remove_queue/{branch_id}/{queue.id}/"
        data = None
        response = self.client.delete(url, data, format=_format)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        