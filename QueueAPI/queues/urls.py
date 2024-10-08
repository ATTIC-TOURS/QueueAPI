from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.views import service_api, branch_api, queue_api, window_api, status_api, setup_api, printer_api


urlpatterns = [
    path("branches/", branch_api.branch_list),
    path("branch_login/<int:pk>/", branch_api.branch_login),
    path("services/", service_api.service_list),
    path("services/<int:pk>/", service_api.service_detail),
    path("current_queue_stats/<int:pk>/", queue_api.current_queue_stats),
    path("current_queues/<int:pk>/", queue_api.current_queues),
    path("windows/", window_api.window_list),
    path("queue_call/", queue_api.queue_call),
    path("viewable_status/", status_api.viewable_status),
    path("queue_update/", queue_api.queue_update),
    path("mobile/", setup_api.mobile),
    path("queues/<int:branch_id>/<int:service_id>/", queue_api.queue),
    path("no_queue_waiting_status/<int:branch_id>/<int:service_id>/", queue_api.no_queue_waiting_status),
    path("printer/<int:branch_id>/", printer_api.printer),
    path("printer_status/<str:mac_address>/", printer_api.printer_status),
    path("mobile_status/<str:mac_address>/", setup_api.mobile_status),
]

urlpatterns = format_suffix_patterns(urlpatterns)