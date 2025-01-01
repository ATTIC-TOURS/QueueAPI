from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import ServiceType
from queues.serializers import ServiceTypeSerializer


@api_view(["GET"])
def service_type_list(request, format=None):
    if request.method == "GET":
        service_types = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)
    
@api_view(["GET"])
def service_type_detail_by_category(request, category_id, format=None):
    try:
        service_types = ServiceType.objects.filter(category_id_id=category_id)
    except ServiceType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ServiceTypeSerializer(service_types, many=True)
        return Response(serializer.data)