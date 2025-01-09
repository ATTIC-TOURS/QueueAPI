import json
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class QueueConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.queue_status = self.scope['url_route']['kwargs']['queue_status'] # queue_status -> waiting, in-progress, call
        self.room_name = self.scope['url_route']['kwargs']['branch_id']
        self.roomGroupName = f"{self.queue_status}-queue-{self.room_name}"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
        
        # sends these data first time connected
        if self.queue_status == "waiting":
            queues = await self.get_waiting_queues(self.room_name) 
        elif self.queue_status == "in-progress":
            queues = await self.get_in_progress_queues(self.room_name)
        elif self.queue_status == "controller":
            queues = await self.get_controller_queues(self.room_name)
        elif self.queue_status == "stats":
            queues = await self.get_queue_stats(self.room_name)
        elif self.queue_status == "call":
            queues = None
        if queues:
            await self.send(text_data=json.dumps(queues))
        
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
        
    async def receive(self, text_data):
        pass
    
    async def queue_call(self, event):
        name = event["name"]
        window_name = event["window_name"]
        queue_code = event["queue_code"]
        await self.send(text_data=json.dumps({
            "name": name, 
            "window_name": window_name, 
            "queue_code": queue_code
        }))

    async def queues_update(self, event):
        branch_id = event["branch_id"]
        queue_status = event["queue_status"]
        
        if queue_status == "waiting": # unused
            queues = await self.get_waiting_queues(branch_id)
        elif queue_status == "in-progress":
            queues = await self.get_in_progress_queues(branch_id)
        elif queue_status == "controller":
            queues = await self.get_controller_queues(self.room_name)
        elif self.queue_status == "stats":
            queues = await self.get_queue_stats(self.room_name)
        await self.send(text_data=json.dumps(queues))
        
    @database_sync_to_async
    def get_in_progress_queues(self , branch_id):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="in-progress").id,
            created_at__gte=timezone.now().date()
        )
        queueSerializer = QueueSerializer(queues, many=True) 
        return queueSerializer.data   
    
    # unused 
    @database_sync_to_async
    def get_waiting_queues(self , branch_id):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        )
        queueSerializer = QueueSerializer(queues, many=True) 
        return queueSerializer.data
    
    @database_sync_to_async
    def get_controller_queues(self , branch_id):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        waiting_queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        )
        in_progress_queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="in-progress").id,
            created_at__gte=timezone.now().date()
        )
        queueSerializer = QueueSerializer(waiting_queues.union(in_progress_queues), many=True)
        return queueSerializer.data

    @database_sync_to_async
    def get_queue_stats(self , branch_id):
        from queues.models import Queue, Status
        statuses = Status.objects.all()
        statuses = {status.name: 0 for status in statuses}
        queues = Queue.objects.filter(
            branch_id=branch_id,
            created_at__gte=timezone.now().date()
        )
        for queue in queues:
            queue_status = queue.status.name
            statuses[queue_status] += 1
        statuses["finish"] = statuses["pending"] + statuses["complete"]
        return statuses