from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Marquee
from queues.serializers import MarqueeSerializer


@api_view(["GET"])
def marquee_list(request, branch_id, format=None):
    if request.method == "GET":
        windows = Marquee.objects.filter(branch_id=branch_id)
        serializer = MarqueeSerializer(windows, many=True)
        return Response(serializer.data)