from django.urls import path
from queues.apiviews import category_api


urlpatterns = [
    path("categories", category_api.category_list),
]

# manual testing

# TestCase 1: check if categories are all set
# http http://127.0.0.1:8000/api/queues/v2/categories