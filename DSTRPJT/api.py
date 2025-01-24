from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DSTRPJT
from .serializers import DSTRPJTserialize

@api_view(['GET', 'POST'])
def Dlist(request):
    if request.method == 'GET':
        all_data = DSTRPJT.objects.all()
        data_ser = DSTRPJTserialize(all_data, many=True)
        return Response(data_ser.data)
    elif request.method == 'POST':
        serial = DSTRPJTserialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
