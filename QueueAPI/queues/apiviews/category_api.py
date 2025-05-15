from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Category
from queues.serializers import CategorySerializer


@api_view(["GET"])
def category_list(request, format=None):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)