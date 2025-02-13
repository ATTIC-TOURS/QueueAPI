from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Marquee
from queues.serializers import MarqueeSerializer


@api_view(["GET"])
def marquee_list(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id", None)
        if branch_id is not None:
            marquees = Marquee.objects.filter(branch_id=branch_id)
        else:
            marquees = Marquee.objects.all()
        serializer = MarqueeSerializer(marquees, many=True)
        return Response(serializer.data)