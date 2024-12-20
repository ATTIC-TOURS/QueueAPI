from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.serializers import MobileSerializer
from queues.models import Mobile


@api_view(["POST"])
def mobile(request, format=None):
    mobile = None
    try:
        mobile = Mobile.objects.get(mac_address=request.data["mac_address"])
    except Mobile.DoesNotExist:
        print(f"This is the first attemp of the mobile to setup at branch_id {request.data['branch_id']}")
    if request.method == "POST":
        # if the mobile already exists
        if mobile:
            partial_data = {
                "branch_id": request.data["branch_id"],
                "is_active": True
            }
            serializer = MobileSerializer(mobile, data=partial_data, partial=True)
            print("This is NOT the first attempt of mobile setup")
        else:
            complete_data = {
                "mac_address": request.data["mac_address"],
                "branch_id": request.data["branch_id"],
                "is_active": True
            }
            serializer = MobileSerializer(data=complete_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def mobile_status(request, mac_address, format=None):
    try:
        queue = Mobile.objects.get(mac_address=mac_address)
    except Mobile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        data = {
            "is_active": False
        }
        serializer = MobileSerializer(queue, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Test Case
# ADD A NEW MOBILE PHONE TO THE BRANCH
# http POST http://127.0.0.1:8000/mobile/ mac_address=234.324.324.234.23 branch_id=1

# WHEN MOBILE IS INACTIVE
# http PATCH http://127.0.0.1:8000/mobile_status/234.324.324.234.23/