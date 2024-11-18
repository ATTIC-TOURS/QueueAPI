from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Window, Category, Service
from queues.serializers import QueueSerializer
from django.utils import timezone

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
    

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


def generate_queue_code(service_id, queue_no):
    service = Service.objects.get(id=service_id)
    category = Category.objects.get(id=service.category_id_id)
    return category.name[0].upper() + str(queue_no)

def generate_new_queue(branch_id, service_id, queue_no, name, email):
    
    service = Service.objects.get(id=service_id)
    category_id = Category.objects.get(id=service.category_id_id).id
    
    if email:
    
        return {
            "branch_id": branch_id,
            "category_id": category_id,
            "service_id": service_id,
            "queue_no": queue_no,
            "status_id": Status.objects.get(name="waiting").id,
            "is_called": False,
            "code": generate_queue_code(service_id, queue_no),
            "name": name,
            "email": email
        }
        
    return {
            "branch_id": branch_id,
            "category_id": category_id,
            "service_id": service_id,
            "queue_no": queue_no,
            "status_id": Status.objects.get(name="waiting").id,
            "is_called": False,
            "code": generate_queue_code(service_id, queue_no),
            "name": name,
        }
    

# http POST http://192.168.1.12:8000/queues/1/1/ queue_no=1 name=kenji email=krimssmirk003@gmail.com

@api_view(["POST"])
def queue(request, branch_id, service_id, format=None):
    # request.data -> branch_id, service_id, queue_no
    
    # ------------
    # request.data
    # ------------
    # queue_no
    r_queue_no = request.data["queue_no"]
    # name
    r_name = request.data["name"]
    # email
    r_email = request.data["email"] if "email" in request.data else None
    
    if request.method == "POST":
        new_queue = generate_new_queue(branch_id, service_id, r_queue_no, r_name, r_email)
            
        serializer = QueueSerializer(data=new_queue)
        if serializer.is_valid():
            
            # BEGIN - notify web sockets
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
            # END - notify web sockets
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# http get http://192.168.1.12:8000/branch/1/waiting/service/1/

@api_view(["GET"])
def no_queue_waiting_status(request, branch_id, service_id, format=None):
    
    service = Service.objects.get(id=service_id)
    category = Category.objects.get(id=service.category_id_id)
    queues = Queue.objects.filter(
            branch_id_id=branch_id,
            category_id_id=category.id,
            status_id_id=Status.objects.get(name="waiting").id,
            created_at__gte=timezone.now().date()
        )
    
    if request.method == "GET":
        n_waiting = len(queues)
        return Response({
            "category_name": category.name,
            "service_name": service.name,
            "n_waiting": n_waiting
        })
            
        return Response(None)