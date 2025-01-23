from django.urls import path
from queues.apiviews import service_api, queue_api


urlpatterns = [
    # Services
    path("branches/<int:branch_id>/categories/<int:category_id>/services", service_api.service_by_category),
    
    # no of waiting in mobile UI
    path("branch/<int:branch_id>/waiting/service/<int:service_id>", queue_api.no_queue_waiting_status),
    
    # Queues
    path("queues/<int:branch_id>/<int:service_id>", queue_api.queue),
]