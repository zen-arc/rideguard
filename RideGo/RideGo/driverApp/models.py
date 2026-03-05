from django.db import models
from adminApp.models import Category

from indexapp.models import Driver





class Vehicle(models.Model):
      name=models.CharField(max_length=100)
      image=models.ImageField(upload_to='images/')
      regno=models.CharField(max_length=100)
      category=models.ForeignKey(Category,on_delete=models.CASCADE)
      fuel_type=models.CharField(max_length=100)
      model=models.CharField(max_length=100)
      no_of_seats=models.IntegerField()
      price_per_km=models.IntegerField(null=True, blank=True, default=0)
      driverid=models.ForeignKey(Driver, on_delete=models.CASCADE)
      
      def __str__(self):
         return self.name