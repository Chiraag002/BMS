from django.urls import path
from .views import *

urlpatterns = [
    path('get_services', GetServicesApiView.as_view(), name='get_services'),
    path('add_services', AddServicesApiView.as_view(), name='add_services'),
    path('update_services/<str:pk>', UpdateServicesApiView.as_view(), name='update_services'),
    path('add_booking', BookingsApiView.as_view(), name='add_services'),
    path('get_available_time', GetAvailablilityApiView.as_view(), name='get_available_time'),
]