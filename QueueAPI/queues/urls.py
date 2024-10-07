from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.views import service_api, branch_api


urlpatterns = [
    path("branches/", branch_api.branch_list),
    path("branch_login/<int:pk>/", branch_api.branch_login),
    path("services/", service_api.service_list),
    path("services/<int:pk>/", service_api.service_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)