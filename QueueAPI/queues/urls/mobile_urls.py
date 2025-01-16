from django.urls import path
from queues.apiviews import queue_api, setup_api, printer_api


urlpatterns = [
    # Mobile
    path("mobile", setup_api.mobile),
    path("mobile_status", setup_api.mobile_status),
    # no of waiting in mobile UI
    path("branch/<int:branch_id>/waiting/service/<int:service_id>", queue_api.no_queue_waiting_status),
    
    # Queues
    path("queues/<int:branch_id>/<int:service_id>", queue_api.queue),
        
    # Printer
    path("printer/<int:branch_id>", printer_api.printer),
    path("printer_status", printer_api.printer_status),
]