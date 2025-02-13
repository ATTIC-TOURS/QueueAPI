from django.urls import path
from queues.apiviews import service_api, queue_api


urlpatterns = [
    # Services
    path("branches/<int:branch_id>/categories/<int:category_id>/services", service_api.service_by_category),
    
    # Queues
    path("queues/<int:branch_id>/<int:service_id>", queue_api.queue),
    
    # new generating a queue
    path("queues", queue_api.new_queue_list),
]