from django.urls import path
from queues.apiviews import service_api


urlpatterns = [
    path("services", service_api.service_list),
    path("services/<int:pk>", service_api.service_detail),
]

# manual testing

# TestCase 1: check if services are all set
# http http://127.0.0.1:8000/api/queues/v2/services

# TestCase 2: check if a distinct service is able to get
# http http://127.0.0.1:8000/api/queues/v2/services/1