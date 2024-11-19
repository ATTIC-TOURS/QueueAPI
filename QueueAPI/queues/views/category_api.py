from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Category
from queues.serializers import CategorySerializer


GET = "GET"

@api_view([GET])
def category_list(request, format=None):
    if request.method == GET:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
@api_view([GET])
def category_detail(request, category_id, format=None):
    if request.method == GET:
        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
# http GET  http://192.168.1.12:8000/categories/1/