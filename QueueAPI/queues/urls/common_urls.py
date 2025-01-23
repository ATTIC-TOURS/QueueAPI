from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.apiviews import category_api, service_api, branch_api
from queues.urls import mobile_urls, controller_urls, tv_urls


urlpatterns = [
    # branch api
    path("branches", branch_api.branch_list),
    path("branch_login/<int:branch_id>", branch_api.branch_login),
    
    # category api
    path("categories/<int:category_id>", category_api.category_detail),
    path("branches/<int:branch_id>/categories", category_api.category_list),
    
    # service api
    path("branches/<int:branch_id>/services", service_api.service_list),
    path("services/<int:pk>", service_api.service_detail),
]