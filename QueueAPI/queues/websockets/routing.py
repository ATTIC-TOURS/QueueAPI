from django.urls import re_path, path
from queues.websockets.consumers import QueueConsumer


websocket_urlpatterns = [
    path("queue-services/v1/current-queues/<str:queue_status>/<int:branch_id>", QueueConsumer.as_asgi()), 
] 