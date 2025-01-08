from django.db import models
from datetime import timedelta,timezone

# Create your models here.
class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    
    class Meta:
        db_table ='services'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    services = models.ForeignKey(Services,on_delete=models.CASCADE,
                                related_name='service',
                                related_query_name='services')
    meeting_link = models.CharField(max_length=256,null=True,blank=True)

    class Meta:
        db_table = 'bookings'
