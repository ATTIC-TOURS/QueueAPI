from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Branch
from queues.serializers import BranchSerializer


GET = "GET"
POST = "POST"

@api_view([GET])
def branch_list(request, format=None):
    if request.method == GET:
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

@api_view([POST])
def branch_login(request, pk, format=None):
    
    password_entered = request.data["password"]
    
    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == POST:
        return Response(
            {
                "status": password_entered == branch.password
            }
        )