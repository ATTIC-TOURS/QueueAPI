from django.urls import path
from queues.apiviews import queue_api, markqueue_api


urlpatterns = [
    # Queues
    path("branches/<int:branch_id>/tv/now-serving", queue_api.tv_now_serving),
    
    # Marquees
    path("markqueues/<int:branch_id>", markqueue_api.markqueue_list),
]