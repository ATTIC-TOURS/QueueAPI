from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Window
from queues.serializers import QueueSerializer
from django.utils import timezone

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
    

# @api_view(["GET"])
# def current_queue_stats(request, branch_id, format=None):
#     statuses = Status.objects.all()
#     statuses = {status.name: 0 for status in statuses}
#     if request.method == "GET":
#         queues = Queue.objects.filter(
#             branch_id=branch_id,
#             created_at__gte=timezone.now().date()
#         )
#         for queue in queues:
#             queue_status = queue.status_id.name
#             statuses[queue_status] += 1
#         statuses["finish"] = statuses["pending"] + statuses["complete"]
#         return Response(statuses)


# @api_view(["GET"])
# def current_queues(request, branch_id, format=None):
#     if request.method == "GET":
#         waiting_queues = Queue.objects.filter(
#             branch_id=branch_id,
#             status_id=Status.objects.get(name="waiting").id,
#             created_at__gte=timezone.now().date()
#         )
#         in_progress_queues = Queue.objects.filter(
#             branch_id=branch_id,
#             status_id=Status.objects.get(name="in-progress").id,
#             created_at__gte=timezone.now().date()
#         )
#         serializer = QueueSerializer(waiting_queues.union(in_progress_queues), many=True)
#         return Response(serializer.data)



@api_view(["PATCH"])
def queue_call(request, branch_id, queue_id, format=None):
    # request.data -> queue_id, window_id
    try:
        queue = Queue.objects.get(pk=queue_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        data = {
            "window_id": request.data["window_id"],
            "status_id": Status.objects.filter(name="in-progress").values().first()["id"],
            "is_called": True,
            "updated_at": timezone.now()
        }
        serializer = QueueSerializer(queue, data=data, partial=True)
        if serializer.is_valid():
            name = queue.name
            window_name = Window.objects.get(id=request.data["window_id"]).name
            queue_code = queue.code
            # ------------Web Socket (Begin)------------ #
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"waiting-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "waiting"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"in-progress-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "in-progress"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"stats-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "stats"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"controller-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "controller"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"call-queue-{branch_id}", 
                {
                    "type": "update_call_applicant",
                    "name": name,
                    "window_name": window_name,
                    "queue_code": queue_code
                }
            )
            # ------------Web Socket (End)------------ #
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def queue_update(request, branch_id, format=None):
    # request.data -> queue_id, status_id
    try:
        queue = Queue.objects.get(pk=request.data["queue_id"])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        updated_data = {
            "status_id": request.data["status_id"]
        }
        serializer = QueueSerializer(queue, data=updated_data, partial=True)
        if serializer.is_valid():
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"waiting-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "waiting"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"in-progress-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "in-progress"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"stats-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "stats"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"controller-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "controller"
                }
            )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def queue(request, branch_id, service_id, format=None):
    # request.data -> branch_id, service_id, queue_no
    if request.method == "POST":
        new_queue_data = {
            "branch_id": branch_id,
            "service_id": service_id,
            # "window_id": None,
            "queue_no": request.data["queue_no"],
            "status_id": Status.objects.get(name="waiting").id,
            "is_called": False,
            "code": Service.objects.get(id=service_id).name[0].upper() + str(request.data["queue_no"]),
            "name": request.data["name"],
        }
        if "email" in request.data:
            new_queue_data["email"] = request.data["email"]
        serializer = QueueSerializer(data=new_queue_data)
        if serializer.is_valid():
            # update_ws_queues("waiting", branch_id)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"waiting-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "waiting"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"in-progress-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "in-progress"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"stats-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "stats"
                }
            )
            async_to_sync(channel_layer.group_send)(
                f"controller-queue-{branch_id}", 
                {
                    "type": "update_queues",
                    "branch_id": branch_id,
                    "queue_status": "controller"
                }
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def no_queue_waiting_status(request, branch_id, service_id, format=None):
    if request.method == "GET":
        queues = Queue.objects.filter(
            branch_id=branch_id,
            service_id=service_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        )
        print(queues)
        no_waiting_status = len(queues)
        return Response(no_waiting_status)


# @api_view(["GET"])
# def in_progress_queues(request, branch_id, format=None):
#     if request.method == "GET":
#         queues = Queue.objects.filter(
#             branch_id=branch_id,
#             status_id=Status.objects.get(name="in-progress").id,
#             created_at__gte=timezone.now().date()
#         )
#         serializer = QueueSerializer(queues, many=True)
#         return Response(serializer.data)


# @api_view(["GET"])
# def waiting_queues(request, branch_id, format=None):
#     if request.method == "GET":
#         queues = Queue.objects.filter(
#             branch_id=branch_id,
#             status_id=Status.objects.get(name="waiting").id,
#             created_at__gte=timezone.now().date()
#         )
#         serializer = QueueSerializer(queues, many=True)
#         return Response(serializer.data)


# ----------------
# web test case
# ----------------
# GET CURRENT QUEUE STATS
# http GET http://127.0.0.1:8000/current_queue_stats/1/

# GET CURRENT QUEUES
# http GET http://127.0.0.1:8000/current_queues/1/

# CALL APPLICANT
# http POST http://127.0.0.1:8000/queue_call/ queue_id=1 window_id=1

# UPDATE A QUEUE
# http PATCH http://127.0.0.1:8000/queue_update/ queue_id=1 status_id=1

# ----------------
# mobile test case
# ----------------
# CREATE A NEW QUEUE
# http POST http://127.0.0.1:8000/queues/1/1/ queue_no=4

# GET THE NO OF WAITING STATUS
# http GET http://127.0.0.1:8000/no_queue_waiting_status/1/1/

# GET THE SERVICES
# http GET http://127.0.0.1:8000/services/

# -------------
# TV test case
# -------------
# GET IN PROGRESS QUEUES
# http GET http://127.0.0.1:8000/in_progress_queues/1/

# GET WAITING QUEUES
# http GET http://127.0.0.1:8000/waiting_queues/1/