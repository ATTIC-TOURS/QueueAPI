from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Window, Category, Branch
from queues.serializers import QueueSerializer
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from queues import email
import datetime


def get_starting_of_current_manila_timezone():
        year = timezone.now().now().year
        month = timezone.now().now().month
        day = timezone.now().now().day
        aware_dt = datetime.datetime(year, month, day-1, 16, tzinfo=datetime.timezone.utc)
        return aware_dt

@api_view(["GET"])
def tv_now_serving(request, branch_id, format=None):
    if request.method == "GET":
        queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="in-progress").id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
        queueSerializer = QueueSerializer(queues, many=True) 
        return Response(queueSerializer.data, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def controller_queues(request, branch_id, format=None):
    if request.method == "GET":
        waiting_queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
        in_progress_queues = Queue.objects.filter(
            branch_id=branch_id,
            status_id=Status.objects.get(name="in-progress").id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
        queueSerializer = QueueSerializer(waiting_queues.union(in_progress_queues), many=True)
        return Response(queueSerializer.data, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def current_queue_stats(request, branch_id, format=None):
    if request.method == "GET":
        statuses = Status.objects.all()
        statuses = {status.name: 0 for status in statuses}
        queues = Queue.objects.filter(
            branch_id=branch_id,
            created_at__gte=get_starting_of_current_manila_timezone()
        )
        for queue in queues:
            queue_status = queue.status_id.name
            statuses[queue_status] += 1
        statuses["finish"] = statuses["pending"] + statuses["complete"]
        return Response(statuses, status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def queue_call(request, branch_id, queue_id, format=None):
    # request.data -> queue_id, window_id
    try:
        queue = Queue.objects.get(pk=queue_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        data = {
            "window": request.data["window_id"],
            "status": Status.objects.filter(name="in-progress").values().first()["id"],
            "is_called": True,
            "updated_at": timezone.now()
        }
        queueSerializer = QueueSerializer(queue, data=data, partial=True)
        if queueSerializer.is_valid():            
            queueSerializer.save()
            return Response(queueSerializer.data)
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def queue_update(request, branch_id, format=None):
    # request.data -> queue_id, status_id
    try:
        queue = Queue.objects.get(pk=request.data["queue_id"])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        updated_data = {
            "status": request.data["status_id"]
        }
        serializer = QueueSerializer(queue, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_queue_code(service_id, queue_no, is_senior_pwd):
    service = Service.objects.get(id=service_id)
    category = Category.objects.get(id=service.category_id)
    code = category.name[0].upper() + str(queue_no)
    if is_senior_pwd:
        return code + " (Senior/PWD)"
    return code

def mobile_queue_status(serializedData):
    branch = Branch.objects.get(id=serializedData["branch"])
    category = Category.objects.get(id=serializedData["category"])
    service = Service.objects.get(id=serializedData["service"])
    
    code = serializedData["code"].split()[0]

    data_for_mobile = {
        "id": serializedData["id"],
        "branch_name": branch.name,
        "category_name": category.name,
        "service_name": service.name,
        "queue_no": serializedData["queue_no"],
        "status_id": serializedData["status"],
        "is_called": serializedData["is_called"],
        "code": code,
        "name": serializedData["name"]
    }
    if "email" not in serializedData:
        return data_for_mobile 
    data_for_mobile["email"] = serializedData["email"]
    return data_for_mobile
        
def generate_new_queue(branch_id, service_id, queue_no, name, email, is_senior_pwd): 
    service = Service.objects.get(id=service_id)
    category_id = Category.objects.get(id=service.category_id).id
    if email:
    
        return {
            "branch": branch_id,
            "category": category_id,
            "service": service_id,
            "queue_no": queue_no,
            "status": Status.objects.get(name="waiting").id,
            "is_called": False,
            "code": generate_queue_code(service_id, queue_no, is_senior_pwd),
            "name": name,
            "email": email,
            "is_senior_pwd": is_senior_pwd
        }
        
    return {
            "branch": branch_id,
            "category": category_id,
            "service": service_id,
            "queue_no": queue_no,
            "status": Status.objects.get(name="waiting").id,
            "is_called": False,
            "code": generate_queue_code(service_id, queue_no, is_senior_pwd),
            "name": name,
            "is_senior_pwd": is_senior_pwd
        }

@api_view(["POST"])
def queue(request, branch_id, service_id, format=None):    
    r_queue_no = request.data["queue_no"]
    r_name = request.data["name"]
    r_email = request.data["email"] if "email" in request.data else None
    r_is_senior_pwd = request.data["is_senior_pwd"]
    
    if request.method == "POST":
        new_queue = generate_new_queue(branch_id, service_id, r_queue_no, r_name, r_email, r_is_senior_pwd)
        queueSerializer = QueueSerializer(data=new_queue)
        if queueSerializer.is_valid():
            new_queue = queueSerializer.save()
            # ----- EMAIL (BEGIN) ------
            # if r_email:
            #     queue_info = {
            #         "name": new_queue.name,
            #         "queue_code": new_queue.code,
            #         "datetime": new_queue.created_at,
            #         "category_name": new_queue.category_id.name,
            #         "service_name": new_queue.service_id.name
            #     }
            #     email.send_greetings(r_email, queue_info)              
            # ----- EMAIL (END) --------
            return Response(
                    mobile_queue_status(queueSerializer.data), 
                    status=status.HTTP_201_CREATED
                )
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def queue_pax(request, queue_id, format=None):
    try:
        queue = Queue.objects.get(pk=queue_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        queueSerializer = QueueSerializer(queue, data={"pax": request.data["pax"]}, partial=True)
        if queueSerializer.is_valid():
            queueSerializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def queue_detail(request, branch_id, queue_id, format=None):
    try:
        queue = Queue.objects.get(pk=queue_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def no_queue_waiting_status(request, branch_id, service_id, format=None):
    
    service = Service.objects.get(id=service_id)
    category = Category.objects.get(id=service.category_id)
    
    # Get a timezone-aware datetime for the start of today
    start_of_today = timezone.localtime(timezone.now()).replace(hour=0, minute=0, second=0, microsecond=0)
    queues = Queue.objects.filter(
            branch_id=branch_id,
            category_id=category.id,
            status_id=Status.objects.get(name="waiting").id,
            created_at__gte=start_of_today
        )
    
    if request.method == "GET":
        n_waiting = len(queues)
        return Response({
            "category_name": category.name,
            "service_name": service.name,
            "n_waiting": n_waiting
        })
            
        return Response(None)