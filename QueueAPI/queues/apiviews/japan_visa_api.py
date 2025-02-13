from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Service, Category
from queues.serializers import ServiceSerializer
from queues.seeds import constants


@api_view(["GET"])
def visa_type_list(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id", None)
        try:
            japan_visa_category = Category.objects.get(branch_id=branch_id, name="JAPAN VISA")
            services = Service.objects.filter(
                branch_id=branch_id,
                category=japan_visa_category
            )
        except Category.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        except Service.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PATCH"])
def visa_type_detail(request, pk, format=None):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PATCH":
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)