from django.test import TestCase
from queues.models import Queue, Branch, Category, Service
from django.utils import timezone
from datetime import timedelta


class DateTimeTest(TestCase):
    
    """terms
    cq: current queue
    pq: past queue
    fq: future queue
    """
    
    @classmethod
    def setUpTestData(cls):
        mainoffice = Branch.objects.get(name="Main Office")
        jvisa = Category.objects.get(name="JAPAN VISA", branch=mainoffice)
        tourist = Service.objects.get(name="Tourism", branch=mainoffice)
        applicant_name = "Kenji"
        no_applicant = 3
        
        # CURRENT
        cls.cq = Queue.objects.create(
            branch=mainoffice,
            category=jvisa,
            service=tourist,
            applicant_name=applicant_name,
            no_applicant=no_applicant
        )
        
        # PAST
        past_datetime = timezone.now() - timedelta(days=1)
        cls.pq = Queue.objects.create(
            branch=mainoffice,
            category=jvisa,
            service=tourist,
            applicant_name=applicant_name,
            no_applicant=no_applicant,
            created_at=past_datetime
        )
        
        # FUTURE
        future_datetime = timezone.now() + timedelta(days=1)
        cls.fq = Queue.objects.create(
            branch=mainoffice,
            category=jvisa,
            service=tourist,
            applicant_name=applicant_name,
            no_applicant=no_applicant,
            created_at=future_datetime
        )
        
    
    def test_get_current_queue(self):
        current_queues = Queue.objects.filter(
            branch=Branch.objects.get(name="Main Office"),
            created_at__date=timezone.localtime(timezone.now()).date()
        )
        self.assertEqual(current_queues.first(), self.cq)
        self.assertNotEqual(current_queues.first(), self.pq)
        self.assertNotEqual(current_queues.first(), self.fq)
    
    def test_get_past_queue(self):
        past_queues = Queue.objects.filter(
            branch=Branch.objects.get(name="Main Office"),
            created_at__date=timezone.localtime(timezone.now() - timedelta(days=1)).date()
        )
        self.assertEqual(past_queues.first(), self.pq)
        self.assertNotEqual(past_queues.first(), self.cq)
        self.assertNotEqual(past_queues.first(), self.fq)
    
    def test_get_future_queue(self):
        future_queues = Queue.objects.filter(
            branch=Branch.objects.get(name="Main Office"),
            created_at__date=timezone.localtime(timezone.now() + timedelta(days=1)).date()
        )
        self.assertEqual(future_queues.first(), self.fq)
        self.assertNotEqual(future_queues.first(), self.cq)
        self.assertNotEqual(future_queues.first(), self.pq)