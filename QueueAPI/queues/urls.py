from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.apiviews import category_api, service_type_api, service_api, branch_api, queue_api, window_api, status_api, setup_api, printer_api, markqueue_api


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
    
    # Statuses
    path("viewable_status", status_api.viewable_status),
    
    # Mobiles
    path("mobile", setup_api.mobile),
    path("mobile_status", setup_api.mobile_status),
    
    # Queues
    path("queues/<int:branch_id>/<int:service_id>", queue_api.queue),
    path("queue_update/<int:branch_id>", queue_api.queue_update),
    path("queue_call/<int:branch_id>/<int:queue_id>", queue_api.queue_call),
    path("remove_queue/<int:branch_id>/<int:queue_id>", queue_api.queue_detail),
    
    # no of waiting in mobile UI
    path("branch/<int:branch_id>/waiting/service/<int:service_id>", queue_api.no_queue_waiting_status),
    
    path("printer/<int:branch_id>", printer_api.printer),
    path("printer_status", printer_api.printer_status),
   
    # http GET http://127.0.0.1:8000/markqueues/1/
    path("markqueues/<int:branch_id>", markqueue_api.markqueue_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)