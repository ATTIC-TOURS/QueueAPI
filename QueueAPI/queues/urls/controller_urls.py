from django.urls import path
from queues.apiviews import queue_api, status_api, window_api


urlpatterns = [
    # Statuses
    path("viewable_status", status_api.viewable_status),
    
    # Stats
    path("branches/<int:branch_id>/current-queue-stats", queue_api.current_queue_stats),
    
    # Queues
    path("branches/<int:branch_id>/controller-queues", queue_api.controller_queues),
    path("queue_update/<int:branch_id>", queue_api.queue_status_update),
    path("queue_call/<int:branch_id>/<int:queue_id>", queue_api.queue_call),
    path("remove_queue/<int:branch_id>/<int:queue_id>", queue_api.queue_detail),
    
    # new
    path("queues/<int:queue_id>", queue_api.queue_pax),
    
    # Windows
    path("windows", window_api.window_list),
]