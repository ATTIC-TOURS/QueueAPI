import json
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import datetime


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
        
        
        queues = None
        # sends these data first time connected
        if self.queue_status == "waiting":
            queues = await self.get_waiting_queues() 
        elif self.queue_status == "now-serving":
            queues = await self.get_in_progress_queues()
        elif self.queue_status == "controller":
            queues = await self.get_controller_queues()
        elif self.queue_status == "stats":
            queues = await self.get_queue_stats()
        elif self.queue_status == "call":
            queues = None
        elif self.queue_status == "current-tourism-stat":
            queues = await self.get_tourism_stat()

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
        queue_status = event["queue_status"]
        
        if queue_status == "waiting": # unused
            queues = await self.get_waiting_queues()
        elif queue_status == "now-serving":
            queues = await self.get_in_progress_queues()
        elif queue_status == "controller":
            queues = await self.get_controller_queues()
        elif queue_status == "stats":
            queues = await self.get_queue_stats()
        elif queue_status == "current-tourism-stat":
            queues = await self.get_tourism_stat()
            
        await self.send(text_data=json.dumps(queues))
        
    def get_starting_of_current_manila_timezone(self):
        yesterday_dt = timezone.now() - datetime.timedelta(days=1)
        year = yesterday_dt.year
        month = yesterday_dt.month
        day = yesterday_dt.day
        aware_dt = datetime.datetime(year, month, day, 16, tzinfo=datetime.timezone.utc)
        return aware_dt
        
    @database_sync_to_async
    def get_in_progress_queues(self):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        queues = Queue.objects.filter(
            branch_id=self.branch_id,
            status_id=Status.objects.get(name="now-serving").id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        queueSerializer = QueueSerializer(queues, many=True) 
        return queueSerializer.data   
    
    # unused 
    @database_sync_to_async
    def get_waiting_queues(self):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        queues = Queue.objects.filter(
            branch_id=self.branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        queueSerializer = QueueSerializer(queues, many=True) 
        return queueSerializer.data
    
    @database_sync_to_async
    def get_controller_queues(self):
        from queues.models import Queue, Status
        from queues.serializers import QueueSerializer
        waiting_queues = Queue.objects.filter(
            branch_id=self.branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        in_progress_queues = Queue.objects.filter(
            branch_id=self.branch_id,
            status_id=Status.objects.get(name="now-serving").id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        queueSerializer = QueueSerializer(waiting_queues.union(in_progress_queues), many=True)
        return queueSerializer.data

    @database_sync_to_async
    def get_queue_stats(self):
        from queues.models import Queue, Status
        statuses = Status.objects.all()
        statuses = {status.name: 0 for status in statuses}
        queues = Queue.objects.filter(
            branch_id=self.branch_id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        for queue in queues:
            queue_status = queue.status.name
            statuses[queue_status] += queue.pax
        statuses["finish"] = statuses["pending"] + statuses["complete"]
        return statuses
    
    @database_sync_to_async
    def get_tourism_stat(self):
        
        from queues.models import Queue, Status, Service
        
        service_id = Service.objects.get(branch_id=self.branch_id, name="Tourism").id
        
        complete_status_id = Status.objects.get(name="complete").id
        queues_complete_tourism = Queue.objects.filter(
            branch_id=self.branch_id,
            service_id=service_id,
            status_id=complete_status_id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        
        complete_tourism_total = 0
        for queue in queues_complete_tourism:
            complete_tourism_total += queue.pax
            
        now_serving_status_id = Status.objects.get(name="now-serving").id
        queues_now_serving_tourism = Queue.objects.filter(
            branch_id=self.branch_id,
            service_id=service_id,
            status_id=now_serving_status_id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        
        now_serving_tourism_total = 0
        for queue in queues_now_serving_tourism:
            now_serving_tourism_total += queue.pax
            
        waiting_status_id = Status.objects.get(name="waiting").id
        queues_waiting_tourism = Queue.objects.filter(
            branch_id=self.branch_id,
            service_id=service_id,
            status_id=waiting_status_id,
            created_at__gte=self.get_starting_of_current_manila_timezone()
        )
        
        waiting_tourism_total = 0
        for queue in queues_waiting_tourism:
            waiting_tourism_total += queue.pax
        
        quota = Service.objects.get(branch_id=self.branch_id, name="Tourism").quota
            
        return {
            "complete": complete_tourism_total,
            "now-serving": now_serving_tourism_total,
            "waiting": waiting_tourism_total,
            "total": complete_tourism_total + now_serving_tourism_total + waiting_tourism_total,
            "quota": quota
        }