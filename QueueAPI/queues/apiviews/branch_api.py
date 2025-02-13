from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Branch
from queues.serializers import BranchSerializer


@api_view(["GET"])
def branch_list(request, format=None):
    if request.method == "GET":
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def branch_login(request, format=None):
    try:
        branch = Branch.objects.get(pk=request.data["branch_id"])
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "POST":
        return Response(
            { "login_status": request.data["password"] == branch.password },
            status=status.HTTP_200_OK
        )