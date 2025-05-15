from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Category, Branch
from queues.serializers import QueueSerializer
from django.utils import timezone


def mobile_queue_status(serialized_data):
    branch = Branch.objects.get(id=serialized_data["branch"])
    service = Service.objects.get(id=serialized_data["service"])

    return {
        "branch_name": branch.name,
        "category_name": service.category.name,
        "service_name": service.name,
        "service_type": serialized_data["service_type"],
        "queue_no": serialized_data["queue_no"],
        "queue_code": serialized_data["queue_code"],
        "applicant_name": serialized_data["applicant_name"],
        "applicant_type": serialized_data["applicant_type"],
        "coordinator_name": serialized_data["coordinator_name"],
        "no_applicant": serialized_data["no_applicant"],
        "created_at": serialized_data["created_at"]
    }

@api_view(["GET", "POST"])
def queue_list(request, format=None):
    if request.method == "GET":
        try:
            branch_id = request.GET.get("branch_id", None)
            if branch_id is not None:
                queues = Queue.objects.filter(
                    branch_id=branch_id,
                    created_at__date=timezone.localtime(timezone.now()).date()
                )
            else:
                queues = Queue.objects.all()
        except Queue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QueueSerializer(queues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == "POST":
        queueSerializer = QueueSerializer(data=request.data)
        if queueSerializer.is_valid():
            queueSerializer.save()
            return Response(mobile_queue_status(queueSerializer.data), status=status.HTTP_201_CREATED)
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def queue_detail(request, pk):
    """
    Retrieve, update or delete a queue.
    """
    try:
        queue = Queue.objects.get(pk=pk)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QueueSerializer(queue)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = QueueSerializer(queue, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)