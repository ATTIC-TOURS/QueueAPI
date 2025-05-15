from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.urls import queue, category, service, status, branch


urlpatterns = (
    queue.urlpatterns + 
    category.urlpatterns + 
    service.urlpatterns +
    status.urlpatterns +
    branch.urlpatterns
)

urlpatterns = format_suffix_patterns(urlpatterns)