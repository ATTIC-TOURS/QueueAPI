from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Service
from queues.serializers import ServiceSerializer


@api_view(["GET"])
def service_list(request, format=None):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def service_detail(request, pk):
    """
    Retrieve, update or delete a service.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

   