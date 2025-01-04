from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Printer
from queues.serializers import PrinterSerializer


@api_view(["POST"])
def printer(request, branch_id, format=None):
    # request.data -> printer_info
    try:
        printer = Printer.objects.get(mac_address=request.data["mac_address"])
    except Printer.DoesNotExist:
        printer = None
    if request.method == "POST":
        # if the printer is already exist
        if printer:
            printer_data = {
                "is_active": True,
                "branch_id": branch_id
            }
            serializer = PrinterSerializer(printer, data=printer_data, partial=True)
        else:
            new_printer_data = {
                "mac_address": request.data["mac_address"],
                "is_active": True,
                "branch_id": branch_id
            }
            serializer = PrinterSerializer(data=new_printer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def printer_status(request, format=None):
    # request.data -> error_msg, mac_address
    try:
        queue = Printer.objects.get(mac_address=request.data["mac_address"])
    except Printer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        data = {
            "error_msg": request.data["error_msg"],
            "is_active": False
        }
        serializer = PrinterSerializer(queue, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)