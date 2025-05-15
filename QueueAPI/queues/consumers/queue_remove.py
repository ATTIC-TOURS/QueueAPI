from channels.generic.websocket import AsyncJsonWebsocketConsumer


class QueueRemoveConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        branch_id = self.scope["url_route"]["kwargs"]["branch_id"]
        self.group_name = f"queue_remove_branch_{branch_id}"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        pass
    
    async def receive_json(self, content):       
        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, {"type": "queue.remove.message", "message": content}
        )
    
    async def queue_remove_message(self, event):
        message = event["message"]
        
        # Send message to WebSocket
        await self.send_json(message)