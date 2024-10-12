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
        return Response(serializer.data)


@api_view(["POST"])
def branch_login(request, pk, format=None):
    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "POST":
        print(request.data)
        if branch.password == request.data["password"]:
            return Response({"status": True})
        return Response({"status": False})


# mobile test case
# http GET http://127.0.0.1:8000/branches/
# http POST http://127.0.0.1:8000/branch_login/1/ password=1111
