from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Category, Branch
from queues.serializers import QueueSerializer


@api_view(["GET"])
def tv_now_serving(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id")
        queues = Queue.get_current_now_serving_queues(branch_id)
        queueSerializer = QueueSerializer(queues, many=True) 
        return Response(queueSerializer.data, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def controller_queues(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id")
        waiting_queues = Queue.get_current_waiting_queues(branch_id)
        now_serving_queues = Queue.get_current_now_serving_queues(branch_id)
        queueSerializer = QueueSerializer(waiting_queues.union(now_serving_queues), many=True)
        return Response(queueSerializer.data, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def current_queue_stats(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id")
        statuses = Status.objects.all()
        statuses = {status.name: 0 for status in statuses}
        queues = Queue.get_current_queues(branch_id)
        for queue in queues:
            queue_status = queue.status_id.name
            statuses[queue_status] += 1
        statuses["finish"] = statuses["pending"] + statuses["complete"]
        return Response(statuses, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

def mobile_queue_status(serialized_data):
    branch = Branch.objects.get(id=serialized_data["branch"])
    category = Category.objects.get(id=serialized_data["category"])
    service = Service.objects.get(id=serialized_data["service"])

    return {
        "branch_name": branch.name,
        "category_name": category.name,
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
def new_queue_list(request, format=None):
    if request.method == "GET":
        try:
            branch_id = request.GET.get("branch_id", None)
            if branch_id is not None:
                queues = Queue.objects.filter(branch_id=branch_id)
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
def new_queue_detail(request, pk):
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