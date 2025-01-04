from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from icecream import ic 

# Create your views here.
class GetServicesApiView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class AddServicesApiView(CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class UpdateServicesApiView(RetrieveUpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class GetAvailablilityApiView(APIView):
    def get(self, request):
        date = request.GET.get('date')
        time_slots = Booking.objects.filter(date=date)
        serializer = BookingSerializer(time_slots, many=True)
        return Response(serializer.data)


class BookingsApiView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer