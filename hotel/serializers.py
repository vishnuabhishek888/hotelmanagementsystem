from rest_framework import serializers
from .models import Category, Room, Booking

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
