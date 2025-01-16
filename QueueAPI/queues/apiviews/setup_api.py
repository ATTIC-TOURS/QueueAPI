from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.serializers import MobileSerializer
from queues.models import Mobile


@api_view(["POST"])
def mobile(request, format=None):
    try:
        mobile = Mobile.objects.get(mac_address=request.data["mac_address"])
    except Mobile.DoesNotExist:
        mobile = None
    if request.method == "POST":
        # if the mobile already exists
        if mobile:
            partial_data = {
                "branch": request.data["branch_id"],
                "is_active": True
            }
            serializer = MobileSerializer(mobile, data=partial_data, partial=True)
        else:
            complete_data = {
                "mac_address": request.data["mac_address"],
                "branch": request.data["branch_id"],
                "is_active": True
            }
            serializer = MobileSerializer(data=complete_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PATCH"])
def mobile_status(request, format=None):
    try:
        queue = Mobile.objects.get(mac_address=request.data["mac_address"])
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