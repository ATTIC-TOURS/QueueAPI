from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.apiviews import category_api, service_api, branch_api, status_api, queue_api, japan_visa_api


urlpatterns = [
    # new branch api
    path("branches", branch_api.branch_list),
    path("branch_login", branch_api.branch_login),
    
    # new category api
    path("categories", category_api.category_list),
    path("categories/<int:pk>", category_api.category_detail),
    
    # service api
    path("services", service_api.service_list),
    path("services/<int:pk>", service_api.service_detail),
    
    # Statuses
    path("statuses", status_api.statuses),
    
    # Stats
    path("current-queue-stats", queue_api.current_queue_stats),
    

    path("controller-queues", queue_api.controller_queues),

    # TV NOW SERVING
    path("tv-now-serving-queues", queue_api.tv_now_serving),
    
    # Japan Visa Types
    path("japan-visa-types", japan_visa_api.visa_type_list),
    path("japan-visa-types/<int:pk>", japan_visa_api.visa_type_detail),
]