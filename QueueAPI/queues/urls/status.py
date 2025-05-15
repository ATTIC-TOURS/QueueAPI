from django.urls import path
from queues.apiviews import status_api


urlpatterns = [
    path("statuses", status_api.statuses),
]

# manual testing

# TestCase 1: check if statuses are all set
# http http://127.0.0.1:8000/api/queues/v2/statuses