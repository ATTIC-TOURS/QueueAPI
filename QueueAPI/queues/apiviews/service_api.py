from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Service, Queue, Status
from queues.serializers import ServiceSerializer
from queues.apiviews.utils.time import get_starting_of_current_manila_timezone


def update_service_cut_off(branch_id, service_id):
    
    # SERVICE QUOTA (temp)
    SERVICE_QUOTA = Service.objects.get(id=service_id).quota
    
    # 1. Get all services which status is complete
    complete_status_id = Status.objects.get(name="complete").id
    complete_service_queues = Queue.objects.filter(
        branch_id=branch_id,
        service_id=service_id,
        status_id=complete_status_id,
        created_at__gte=get_starting_of_current_manila_timezone()
    )
    
    # 2. Count the total pax
    complete_service_total_pax = 0
    for queue in complete_service_queues:
        complete_service_total_pax += queue.pax
    
    # 3. Determine if the service is still available     
    service = Service.objects.get(id=service_id)
    if SERVICE_QUOTA and complete_service_total_pax >= SERVICE_QUOTA:
        service.is_cut_off = True 
    else:
        service.is_cut_off = False
    
    # 4. Update the service
    service.save()

@api_view(["GET"])
def service_list(request, branch_id, format=None):
    if request.method == "GET":
        # --------------- IS CUT OFF (START)------------------------
        tourism_id = Service.objects.get(branch_id=branch_id, name="Tourism").id
        update_service_cut_off(branch_id, tourism_id)
        # --------------- IS CUT OFF (END)--------------------------
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