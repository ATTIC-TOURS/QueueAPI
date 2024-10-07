from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status
from queues.serializers import QueueSerializer
from django.utils import timezone
    

@api_view(["GET"])
def current_queue_stats(request, pk, format=None):
    statuses = Status.objects.all()
    statuses = {status.name: 0 for status in statuses}
    if request.method == "GET":
        queues = Queue.objects.filter(
            branch_id=pk,
            created_at__gte=timezone.now().date()
        )
        for queue in queues:
            queue_status = queue.status_id.name
            statuses[queue_status] += 1
        statuses["finish"] = statuses["pending"] + statuses["complete"]
        return Response(statuses)


@api_view(["GET"])
def current_queues(request, pk, format=None):
    if request.method == "GET":
        queues = Queue.objects.filter(
            branch_id=pk,
            created_at__gte=timezone.now().date()
        )
        serializer = QueueSerializer(queues, many=True)
        return Response(serializer.data)


@api_view(["PATCH"])
def queue_call(request, format=None):
    try:
        queue = Queue.objects.get(pk=request.data["queue_id"])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        data = {
            "window_id": request.data["window_id"],
            "status_id": Status.objects.filter(name="in-progress").values().first()["id"],
            "is_called": True
        }
        serializer = QueueSerializer(queue, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def queue_update(request, format=None):
    try:
        queue = Queue.objects.get(pk=request.data["queue_id"])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        serializer = QueueSerializer(queue, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)