from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Window
from queues.serializers import WindowSerializer


@api_view(["GET"])
def window_list(request, format=None):
    if request.method == "GET":
        windows = Window.objects.all()
        serializer = WindowSerializer(windows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)