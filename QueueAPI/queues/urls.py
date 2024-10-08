from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.views import service_api, branch_api, queue_api, window_api, status_api, setup_api


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
]

urlpatterns = format_suffix_patterns(urlpatterns)