from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.apiviews import category_api, service_type_api, service_api, branch_api, window_api
from queues.urls import mobile_urls, controller_urls, tv_urls


urlpatterns = [
    # branch api
    path("branches", branch_api.branch_list),
    path("branch_login/<int:branch_id>", branch_api.branch_login),
    
    # category api
    path("categories", category_api.category_list),
    path("categories/<int:category_id>", category_api.category_detail),
    
    # service type api
    path("service_types", service_type_api.service_type_list),
    path("service_types/<int:category_id>", service_type_api.service_type_detail_by_category),
    
    # service api
    path("services", service_api.service_list),
    path("services/<int:pk>", service_api.service_detail),
    path("services/category/<int:category_id>", service_api.service_by_category),
    
    # Windows
    path("windows", window_api.window_list),
]

urlpatterns = urlpatterns + mobile_urls.urlpatterns + controller_urls.urlpatterns + tv_urls.urlpatterns

urlpatterns = format_suffix_patterns(urlpatterns)