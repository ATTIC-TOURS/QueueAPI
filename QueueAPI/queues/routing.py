from django.urls import re_path, path
from queues.consumers import QueueConsumer, AnnouncementConsumer


websocket_urlpatterns = [
    path("queue-services/v1/current-queues/<str:queue_status>/<int:branch_id>", QueueConsumer.as_asgi()), 
    path("queue-services/v1/ws/announcement/<int:branch_id>", AnnouncementConsumer.as_asgi()),
] 