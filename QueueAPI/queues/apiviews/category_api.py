from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Category
from queues.serializers import CategorySerializer


@api_view(["GET"])
def category_list(request, format=None):
    if request.method == "GET":
        categories = Category.objects.all()
        categorySerializer = CategorySerializer(categories, many=True)
        return Response(categorySerializer.data)
    
@api_view(["GET"])
def category_detail(request, category_id, format=None):
    if request.method == "GET":
        category = Category.objects.get(pk=category_id)
        categorySerializer = CategorySerializer(category)
        return Response(categorySerializer.data)