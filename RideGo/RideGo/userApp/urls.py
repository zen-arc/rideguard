from django.urls import path

from .import views

urlpatterns = [
    
    path('user_index/', views.user_index, name='user_index'),
    
    path('view_drivers/', views.view_drivers, name='view_drivers'),
    path('view_vehicles/', views.view_vehicles, name='view_vehicles'),
    
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),

    path('trip-booking/<int:vehicle_id>/', views.trip_booking, name='trip_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    
    path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),

    path('add_review/<int:vehicle_id>/', views.add_review, name='add_review'),

    path('bookings/', views.admin_booking_list, name='admin_booking_list'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]
