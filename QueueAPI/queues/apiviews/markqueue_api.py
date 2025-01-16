from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import MarkQueue
from queues.serializers import MarkQueueSerializer


@api_view(["GET"])
def markqueue_list(request, branch_id, format=None):
    if request.method == "GET":
        windows = MarkQueue.objects.filter(branch_id=branch_id)
        serializer = MarkQueueSerializer(windows, many=True)
        return Response(serializer.data)