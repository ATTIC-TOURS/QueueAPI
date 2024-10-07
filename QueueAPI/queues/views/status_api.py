from rest_framework.decorators import api_view
from rest_framework.response import Response
    

@api_view(["GET"])
def viewable_status(request, format=None):
    if request.method == "GET":
        return Response(["Complete", "Pending", "Cancel"])