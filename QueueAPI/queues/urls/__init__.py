from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queues.urls import mobile_urls, controller_urls, tv_urls, common_urls


urlpatterns = common_urls.urlpatterns + mobile_urls.urlpatterns + controller_urls.urlpatterns + tv_urls.urlpatterns

urlpatterns = format_suffix_patterns(urlpatterns)