from django.urls import path

from .import views

urlpatterns = [
    path('adminhome/', views.adminhome, name='adminhome'),
    # Category Management
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),  # Added Edit Category URL
    path('del_category/<int:id>/', views.del_category, name='del_category'),
    
    path('driver_Approved/<int:id>',views.approve_driver,name='approve_driver'),
    path('reject_driver/<int:id>',views.reject_driver,name='reject_driver'),

    path('driver_Approved/',views.driver_Approved,name='driver_Approved'),
    path('driver_Pending/',views.driver_Pending,name='driver_Pending'),
    
    path('view_vehicle/',views.view_vehicle,name='view_vehicle'),

    path("booking_status_report/", views.booking_status_report, name="booking_status_report"),
    path("top_rated_vehicles_report/", views.top_rated_vehicles_report, name="top_rated_vehicles_report"),
    path("driver_availability_report/", views.driver_availability_report, name="driver_availability_report"),
    path("category_wise_vehicle_report/", views.category_wise_vehicle_report, name="category_wise_vehicle_report"),
    
 

]