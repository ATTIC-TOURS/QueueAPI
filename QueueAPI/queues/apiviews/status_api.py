from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Status
from queues.serializers import StatusSerializer
    

@api_view(["GET"])
def statuses(request, format=None):
    if request.method == "GET":
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)