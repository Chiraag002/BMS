from django.core.mail import send_mail
from django.conf import settings
from icecream import ic

def send_booking_confirmation_email(booking):
    guest_name = f"{booking.first_name} {booking.last_name}"
    contact_us = settings.EMAIL_HOST_USER
    subject = f"Booking Confirmation - {guest_name}"
    message = f"Dear {guest_name},\n\nYour booking for {booking.services.service_name} has been confirmed. Your booking details are as follows:\n\nService Type: {booking.services.service_name}\nCheck-in Date: {booking.date}\nJoining time: {booking.start_time}\n\nPlease make sure to contact {contact_us} for any further inquiries or updates.\n\nBest regards,\nBooking System"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [booking.email]
    send_mail(subject, message, from_email, recipient_list)
