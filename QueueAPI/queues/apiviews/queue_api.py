from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Queue, Status, Service, Window, Category, Branch
from queues.serializers import QueueSerializer
from django.utils import timezone


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


# Queue PATCH
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
            "status": Status.objects.filter(name="now-serving").values().first()["id"],
            "is_called": True,
            "called_at": timezone.now()
        }
        queueSerializer = QueueSerializer(queue, data=data, partial=True)
        if queueSerializer.is_valid():            
            queueSerializer.save()
            return Response(queueSerializer.data)
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Queue PATCH
@api_view(["PATCH"])
def queue_status_update(request, branch_id, format=None):
    # request.data -> queue_id, status_id
    try:
        queue = Queue.objects.get(pk=request.data["queue_id"])
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        updated_data = {
            "status": request.data["status_id"],
            "updated_at": timezone.now()
        }
        serializer = QueueSerializer(queue, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_queue_code(service_id, queue_no, is_senior_pwd):
    service = Service.objects.get(id=service_id)
    category = Category.objects.get(id=service.category_id)
    code = f"{category.name[0].upper()}-{service.name[0].upper()}{queue_no}"
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
        
def generate_new_queue(branch_id, service_id, queue_no, name, email, is_senior_pwd, pax): 
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
            "is_senior_pwd": is_senior_pwd,
            "pax": pax
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
            "is_senior_pwd": is_senior_pwd,
            "pax": pax
        }

# Queue POST
@api_view(["POST"])
def queue(request, branch_id, service_id, format=None):    
    r_queue_no = request.data["queue_no"]
    r_name = request.data["name"]
    r_email = request.data["email"] if "email" in request.data else None
    r_is_senior_pwd = request.data["is_senior_pwd"]
    r_pax = request.data["pax"]
    
    if request.method == "POST":
        new_queue = generate_new_queue(branch_id, service_id, r_queue_no, r_name, r_email, r_is_senior_pwd, r_pax)
        queueSerializer = QueueSerializer(data=new_queue)
        if queueSerializer.is_valid():
            new_queue = queueSerializer.save()
            return Response(
                    mobile_queue_status(queueSerializer.data), 
                    status=status.HTTP_201_CREATED
                )
        return Response(queueSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Queue PATCH
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


# Queue DELETE
@api_view(["DELETE"])
def queue_detail(request, branch_id, queue_id, format=None):
    try:
        queue = Queue.objects.get(pk=queue_id)
    except Queue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
            return Response(queueSerializer.data, status=status.HTTP_201_CREATED)
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
    