from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues import views


urlpatterns = [
    path("branches/", views.branch_list),
    path("branch_login/<int:pk>/", views.branch_login),
    path("services/", views.service_list),
    path("services/<int:pk>/", views.service_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)