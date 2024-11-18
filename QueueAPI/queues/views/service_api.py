from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Service
from queues.serializers import ServiceSerializer


GET = "GET"
POST = "POST"
PATCH = "PATCH"
DELETE = "DELETE"

@api_view([GET, POST])
def service_list(request, format=None):
    if request.method == GET:
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    elif request.method == POST:
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view([GET, PATCH, DELETE])
def service_detail(request, pk, format=None):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view([GET])
def service_by_category(request, category_id, format=None):
    try:
        services = Service.objects.filter(category_id_id=category_id)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == GET:
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


# mobile test case
# http GET http://127.0.0.1:8000/services/