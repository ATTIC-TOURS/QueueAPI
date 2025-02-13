from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Category
from queues.serializers import CategorySerializer


@api_view(["GET"])
def category_list(request, format=None):
    if request.method == "GET":
        branch_id = request.GET.get("branch_id", None)
        if branch_id is not None:
            categories = Category.objects.filter(branch_id=branch_id)
        else:
            categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def category_detail(request, pk, format=None):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)