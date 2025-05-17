import json
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class QueueConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.queue_status = self.scope['url_route']['kwargs']['queue_status'] # queue_status -> waiting, now-serving, call
        self.branch_id = self.scope['url_route']['kwargs']['branch_id']
        self.roomGroupName = f"{self.queue_status}-queue-{self.branch_id}"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
        
        # sends these data first time connected
        queues = None
        if self.queue_status == "stats":
            queues = await self.get_queue_stats()

        if queues:
            await self.send(text_data=json.dumps(queues))
        
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
        
    async def receive(self, text_data):
        pass

    async def queues_update(self, event):
        queue_status = event["queue_status"]
        
        if queue_status == "stats":
            queues = await self.get_queue_stats()
        await self.send(text_data=json.dumps(queues))

    @database_sync_to_async
    def get_queue_stats(self):
        from queues.models import Queue, Status
        statuses = Status.objects.all()
        statuses = {status.name: 0 for status in statuses}
        queues = Queue.objects.filter(
            branch_id=self.branch_id,
            created_at__date=timezone.localtime(timezone.now()).date()
        )
        for queue in queues:
            queue_status = queue.status.name
            statuses[queue_status] += queue.no_applicant
        statuses["finish"] = statuses["complete"] + statuses["pending"] + statuses["return"]
        return statuses