from channels.generic.websocket import AsyncJsonWebsocketConsumer


class AnnouncementConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        branch_id = self.scope["url_route"]["kwargs"]["branch_id"]
        self.group_name = f"announcement_branch_{branch_id}"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        await self.accept()
        
        print("Announcement Consumer is instantiated!")
        print(f"{self.channel_name} is added to {self.group_name}")
    
    async def disconnect(self, close_code):
        pass
    
    async def receive_json(self, content):        
        print(f"receive: {content}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, {"type": "announcement.message", "message": content}
        )
    
    async def announcement_message(self, event):
        message = event["message"]
        
        # Send message to WebSocket
        await self.send_json(message)