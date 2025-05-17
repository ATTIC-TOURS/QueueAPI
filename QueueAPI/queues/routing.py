from django.urls import re_path, path
from queues.consumers import QueueConsumer, AnnouncementConsumer, QueueUpdateConsumer, QueueRemoveConsumer, QueueCallConsumer


websocket_urlpatterns = [
    path("api/queues/v2/ws/current-queues/<str:queue_status>/<int:branch_id>", QueueConsumer.as_asgi()), 
    path("api/queues/v2/ws/announcement/<int:branch_id>", AnnouncementConsumer.as_asgi()),
    path("api/queues/v2/ws/queue-update/<int:branch_id>", QueueUpdateConsumer.as_asgi()),
    path("api/queues/v2/ws/queue-remove/<int:branch_id>", QueueRemoveConsumer.as_asgi()),
    path("api/queues/v2/ws/queue-call/<int:branch_id>", QueueCallConsumer.as_asgi()),
] 

# requirements (controller)
# 1 one that gives the updated queue
# 2 one that gives the removed queue
