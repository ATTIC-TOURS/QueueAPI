from django.urls import path
from queues.apiviews import queue_api


urlpatterns = [
    path("queues", queue_api.new_queue_list),
    path("queues/<int:pk>", queue_api.new_queue_detail),
]