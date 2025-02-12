from django.test import TestCase
from queues.models import Queue, Branch, Category, Service, Window, Status


class QueueModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Queue.objects.create(
            branch=Branch.objects.get(id=1),
            category=Category.objects.get(id=1),
            service=Service.objects.get(id=1),
            service_type="Additional Documents",
            window=Window.objects.get(id=1),
            status=Status.objects.get(id=1),
            queue_code="AD-1",
            applicant_name="kenji",
            no_applicant=3,
            applicant_type="Walk-In",
            is_senior_pwd=True,
            queue_no=1,
            coordinator_name="Hazel",
            is_priority=True
        )
    
    def test_branch_is_set(self):
        queue = Queue.objects.get(id=1)
        branch = queue.branch
        self.assertEqual(branch, Branch.objects.get(id=1))