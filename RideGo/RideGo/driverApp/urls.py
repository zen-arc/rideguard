from django.urls import path

from .import views

urlpatterns = [
    
    path('driver_home/',views.driver_home, name='driver_home'),
    
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('edit_vehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),  # Added Edit Vehicle URL
    path('del_vehicle/<int:id>/', views.del_vehicle, name='del_vehicle'),
    
    
    path('booking_list/', views.booking_list, name='booking_list'),    
    path('update-order-status/<int:id>/', views.update_order_status, name='update_order_status'),   
     
    path('edit_driver/', views.edit_driver, name='edit_driver'),


    path('reviews/', views.reviews_list, name='reviews_list'),
    
    path('logout/', views.logout, name='logout'),
    path('drowsiness_feed/', views.drowsiness_feed, name='drowsiness_feed'),
    path('start_detection/', views.start_drowsiness_detection, name='start_detection'),
    path('stop_detection/', views.stop_drowsiness_detection, name='stop_detection'),
]