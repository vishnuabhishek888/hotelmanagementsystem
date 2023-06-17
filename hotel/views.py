from rest_framework import generics
from rest_framework.response import Response
from datetime import date
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

class RoomAvailabilityView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', date.today())
        end_date = self.request.query_params.get('end_date', date.today())

        return Room.objects.exclude(
            booking__start_date__gte=end_date,
            booking__end_date__lte=start_date
        )

class CategoryAvailabilityView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        start_date = self.request.query_params.get('start_date', date.today())
        end_date = self.request.query_params.get('end_date', date.today())

        return Room.objects.filter(
            category_id=category_id
        ).exclude(
            booking__start_date__gte=end_date,
            booking__end_date__lte=start_date
        )

class RoomGuestsView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        guests = Booking.objects.filter(room=instance)
        guest_serializer = BookingSerializer(guests, many=True)
        data = serializer.data
        data['guests'] = guest_serializer.data
        return Response(data)
