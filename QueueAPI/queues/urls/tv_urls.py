from django.urls import path
from queues.apiviews import queue_api, marquee_api


urlpatterns = [
    # Queues
    path("branches/<int:branch_id>/tv/now-serving", queue_api.tv_now_serving),
    
    # Marquees
    path("marquees/<int:branch_id>", marquee_api.marquee_list),
]