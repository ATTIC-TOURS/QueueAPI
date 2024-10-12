import json
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from queues.models import Queue, Status
from queues.serializers import QueueSerializer


class QueueConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.queue_status = self.scope['url_route']['kwargs']['queue_status']
        self.room_name = self.scope['url_route']['kwargs']['branch_id']
        self.roomGroupName = f"{self.queue_status}-queue-{self.room_name}"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self , close_code):
        await self.channel_name.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
        
    async def receive(self, text_data):
        pass

    async def update_queues(self, event):
        branch_id = event["branch_id"]
        queue_status = event["queue_status"]
        if queue_status == "waiting":
            queues = await self.get_waiting_queues(branch_id)
            await self.send(text_data=json.dumps(queues))
        elif queue_status == "in-progress":
            queues = await self.get_in_progress_queues(branch_id)
            await self.send(text_data=json.dumps(queues))
        
    @database_sync_to_async
    def get_in_progress_queues(self , branch_id):
        queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="in-progress").id,
            created_at__gte=timezone.now().date()
        )
        serializer = QueueSerializer(queues, many=True) 
        return serializer.data   
        
    @database_sync_to_async
    def get_waiting_queues(self , branch_id):
        queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        )
        serializer = QueueSerializer(queues, many=True) 
        return serializer.data