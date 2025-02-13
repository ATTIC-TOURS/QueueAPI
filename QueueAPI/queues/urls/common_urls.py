from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.apiviews import category_api, service_api, branch_api
from queues.urls import mobile_urls, controller_urls, tv_urls


urlpatterns = [
    # new branch api
    path("branches", branch_api.branch_list),
    path("branch_login", branch_api.branch_login),
    
    # new category api
    path("categories", category_api.category_list),
    path("categories/<int:pk>", category_api.category_detail),
    
    # service api
    path("branches/<int:branch_id>/services", service_api.service_list),
    path("services/<int:pk>", service_api.service_detail),
]