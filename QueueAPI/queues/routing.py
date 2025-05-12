from django.urls import re_path, path
from queues.consumers import QueueConsumer, AnnouncementConsumer


websocket_urlpatterns = [
    path("api/queues/v2/ws/current-queues/<str:queue_status>/<int:branch_id>", QueueConsumer.as_asgi()), 
    path("api/queues/v2/ws/announcement/<int:branch_id>", AnnouncementConsumer.as_asgi()),
] 