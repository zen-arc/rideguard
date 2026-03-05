from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userreg/', views.userreg, name='userreg'),
    path('userlog/', views.userlog, name='userlog'),
    path('driver_reg/',views.driver_reg, name='driver_reg'),


]
