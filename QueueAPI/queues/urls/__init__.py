from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.urls import common_urls


urlpatterns = common_urls.urlpatterns

urlpatterns = format_suffix_patterns(urlpatterns)