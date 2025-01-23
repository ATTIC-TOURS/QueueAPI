from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Service
from queues.serializers import ServiceSerializer


@api_view(["GET"])
def service_list(request, branch_id, format=None):
    if request.method == "GET":
        services = Service.objects.filter(branch_id=branch_id)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
@api_view(["GET"])
def service_detail(request, pk, format=None):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

@api_view(["GET"])
def service_by_category(request, branch_id, category_id, format=None):
    try:
        services = Service.objects.filter(branch_id=branch_id, category_id=category_id)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)