from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Status
from queues.serializers import StatusSerializer
    

@api_view(["GET"])
def viewable_status(request, format=None):
    if request.method == "GET":
        viewable_statuses = []
        for status_name in ["complete", "pending", "cancel"]:
            status = Status.objects.get(name=status_name)
            viewable_statuses.append(status)
        serializer = StatusSerializer(viewable_statuses, many=True)
        return Response(serializer.data)


# test case
# http GET http://127.0.0.1:8000/viewable_status/