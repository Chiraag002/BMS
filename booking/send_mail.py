from django.core.mail import send_mail
from django.conf import settings
from icecream import ic
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .utils import create_event, get_event_details
from .models import Booking

def send_booking_confirmation_email(booking):
    guest_name = f"{booking.first_name} {booking.last_name}"
    contact_us = settings.EMAIL_HOST_USER
    title = "Sample Meeting"
    description = "Discuss project updates"
    # Create Google Calendar event details
    event_details = get_event_details(title, description,booking.date, booking.start_time, booking.end_time)
    
    # Create event in Google Calendar
    meeting_link = create_event(event_details)
    ic(meeting_link)
    
    subject = f"Booking Confirmation - {guest_name}"
    message = f"Dear {guest_name},\n\nYour booking for {booking.services.service_name} has been confirmed. Your booking details are as follows:\n\nService Type: {booking.services.service_name}\nCheck-in Date: {booking.date}\nJoining time: {booking.start_time}\nmeeting_link : {meeting_link}\n\nPlease make sure to contact {contact_us} for any further inquiries or updates.\n\nBest regards,\nBooking System"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [booking.email]
    ic(booking.pk)
    setattr(booking, 'meeting_link', meeting_link)
    booking.save()
    # send_mail(subject, message, from_email, recipient_list)


# def create_meeting(request):
    
#     start_time = "2025-01-07T10:00:00"
#     end_time = "2025-01-07T11:00:00"
    
    
    
#     if meeting_link:
#         # Send email with meeting link
#         send_mail(
#             'Meeting Invitation: ' + title,
#             f'You are invited to the meeting. Join using the following link:\n{meeting_link}',
#             settings.EMAIL_HOST_USER,
#             ['recipient@example.com'],  # Replace with actual recipient email
#             fail_silently=False,
#         )
#         return HttpResponse("Meeting created and invitation sent!")
#     else:
#         return HttpResponse("Failed to create the meeting.")
