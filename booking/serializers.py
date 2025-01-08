from rest_framework import serializers
from .models import *
from datetime import datetime , timedelta
from django.utils import timezone
from icecream import ic
from .send_mail import send_booking_confirmation_email 


# Write Your Serializer Code here
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        exclude = []

class BookingSerializer(serializers.ModelSerializer):
    start_time = serializers.CharField(required=True)
    end_time = serializers.CharField(required=True)

    class Meta:
        model = Booking
        exclude = [] 

    def convert_12hr_to_24hr_format(self,time_str):
        # Parse the 12-hour time format using strptime
        time_obj = datetime.strptime(time_str, "%I:%M %p").time()  # %I for 12-hour, %M for minutes, %p for AM/PM
        return time_obj

    def to_representation(self, instance:Booking):
        data = super().to_representation(instance)
        data['start_time'] = instance.start_time.strftime("%I:%M %p")
        data['end_time'] = instance.end_time.strftime("%I:%M %p")
        return data

    def validate(self, data):
        # Validate that the booking date is within the next 15 days
        if data['date'] < timezone.now().date() or data['date'] > timezone.now().date() + timedelta(days=15):
            raise serializers.ValidationError("Booking can only be made within a 15-day cycle.")
        return data

    
    def create(self, validated_data):
        # Convert the 12-hour time format to 24-hour format
        validated_data['start_time'] = self.convert_12hr_to_24hr_format(validated_data['start_time'])
        validated_data['end_time'] = (datetime.combine(datetime.today(), validated_data['start_time']) + timedelta(minutes=20)).time()
        booking_data = super().create(validated_data)
        send_booking_confirmation_email(booking_data)
        return booking_data
