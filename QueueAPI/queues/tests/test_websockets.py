from django.test import TestCase
from django.urls import path
from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from queues.consumers import QueueConsumer


class WebsocketConnectionsTest(TestCase):
    
    application = URLRouter([
            path("testws/<queue_status>/<branch_id>", QueueConsumer.as_asgi()),
    ])
    
    async def test_connection_in_progress_queue(self):
        queue_status = "in-progress"
        branch_id = 1
        communicator = WebsocketCommunicator(self.application, f"testws/{queue_status}/{branch_id}")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
    
    async def test_connection_waiting_queue(self):
        queue_status = "waiting"
        branch_id = 1
        communicator = WebsocketCommunicator(self.application, f"testws/{queue_status}/{branch_id}")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
    
    async def test_connection_controller_queue(self):
        queue_status = "controller"
        branch_id = 1
        communicator = WebsocketCommunicator(self.application, f"testws/{queue_status}/{branch_id}")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
    
    async def test_connection_stats_queue(self):
        queue_status = "stats"
        branch_id = 1
        communicator = WebsocketCommunicator(self.application, f"testws/{queue_status}/{branch_id}")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
    
    async def test_connection_call_queue(self):
        queue_status = "call"
        branch_id = 1
        communicator = WebsocketCommunicator(self.application, f"testws/{queue_status}/{branch_id}")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)