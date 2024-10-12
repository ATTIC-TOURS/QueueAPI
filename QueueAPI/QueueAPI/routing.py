from django.urls import path
from QueueAPI.consumers import QueueConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the current queue functionality.
websocket_urlpatterns = [
    path("current_queues/<str:queue_status>/<int:branch_id>/" , QueueConsumer.as_asgi()) , 
] 