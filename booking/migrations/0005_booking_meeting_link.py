# Generated by Django 5.1.4 on 2025-01-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_end_time_booking_start_time_delete_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='meeting_link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
