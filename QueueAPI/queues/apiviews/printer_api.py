from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from queues.models import Printer
from queues.serializers import PrinterSerializer


@api_view(["POST"])
def printer(request, branch_id, format=None):
    # request.data -> printer_info
    printer = None
    try:
        printer = Printer.objects.get(mac_address=request.data["mac_address"])
    except Printer.DoesNotExist:
        print(f"This is the first attempt of adding a new printer at branch {branch_id}")
    if request.method == "POST":
        # if the printer is already exist
        if printer:
            printer_data = {
                "is_active": True,
                "branch_id": branch_id
            }
            serializer = PrinterSerializer(printer, data=printer_data, partial=True)
            print("This is not the first attempt adding a new printer")
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
def printer_status(request, mac_address, format=None):
    # request.data -> error_msg
    try:
        queue = Printer.objects.get(mac_address=mac_address)
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
    

# mobile test case
# CREATE A NEW PRINTER
# http POST http://127.0.0.1:8000/printer/1/ mac_address=123.123.123.123

# WHEN PRINTER IS ERROR
# http PATCH http://127.0.0.1:8000/printer_status/123.123.123.123/ error_msg="paper is empty."