from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.views import category_api, service_type_api, service_api, branch_api, queue_api, window_api, status_api, setup_api, printer_api, markqueue_api


urlpatterns = [
    
    # branch api
    path("branches/", branch_api.branch_list),
    path("branch_login/<int:branch_id>/", branch_api.branch_login),
    
    # category api
    path("categories/", category_api.category_list),
    
    # service type api
    path("service_types/", service_type_api.service_type_list),
    path("service_types/<int:category_id>/", service_type_api.service_type_detail_by_category),
    
    # service api
    path("services/", service_api.service_list),
    path("services/<int:pk>/", service_api.service_detail),
    path("services/category/<int:category_id>/", service_api.service_by_category),
    
    
    
    path("windows/", window_api.window_list),
    path("queue_call/<int:branch_id>/<int:queue_id>/", queue_api.queue_call),
    path("viewable_status/", status_api.viewable_status),
    path("queue_update/<int:branch_id>/", queue_api.queue_update),
    path("mobile/", setup_api.mobile),
    
    # generate new queue
    path("queues/<int:branch_id>/<int:service_id>/", queue_api.queue),
    
    # no of waiting in mobile UI
    path("branch/<int:branch_id>/waiting/service/<int:service_id>/", queue_api.no_queue_waiting_status),
    
    path("printer/<int:branch_id>/", printer_api.printer),
    path("printer_status/<str:mac_address>/", printer_api.printer_status),
    path("mobile_status/<str:mac_address>/", setup_api.mobile_status),
    path("markqueues/<int:branch_id>/", markqueue_api.markqueue_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)