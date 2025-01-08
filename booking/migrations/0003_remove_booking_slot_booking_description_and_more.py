# Generated by Django 5.1.4 on 2025-01-04 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_services_rename_name_booking_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slot',
        ),
        migrations.AddField(
            model_name='booking',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='services',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='service', related_query_name='services', to='booking.services'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslot',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', related_query_name='bookings', to='booking.booking'),
        ),
    ]
