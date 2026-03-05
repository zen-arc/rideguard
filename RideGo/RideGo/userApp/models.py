from django.db import models
from .utils import reverse_geocode
from driverApp.models import Vehicle  # Import related models
from indexapp.models import tblUserReg, Driver  # Import related models
#from .views import reverse_geocode
from django.core.exceptions import ValidationError

class Booking(models.Model):
    userid = models.ForeignKey(tblUserReg, on_delete=models.CASCADE)  # User who booked the trip
    vehicleid = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Vehicle used for the trip
    driverid = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)  # Driver assigned

    from_location = models.CharField(max_length=255)
    from_location_name = models.CharField(max_length=255, blank=True, null=True) 
    destination_location = models.CharField(max_length=255)
    destination_location_name = models.CharField(max_length=255, blank=True, null=True) 
    travel_date = models.DateField()
    travel_time = models.TimeField()

    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    payment_status = models.CharField(max_length=20, default='unpaid')

    def clean(self):
        """Prevent duplicate bookings for the same vehicle on the same date and time."""
        existing_booking = Booking.objects.filter(
            vehicleid=self.vehicleid,
            travel_date=self.travel_date,
            travel_time=self.travel_time
        ).exclude(id=self.id)  # Exclude current instance for updates

        if existing_booking.exists():
            raise ValidationError("This vehicle is already booked for the selected date and time.")

    def save(self, *args, **kwargs):
        # Reverse geocode "From" location
        if self.from_location and not self.from_location_name:
            lat, lon = map(float, self.from_location.split(','))
            self.from_location_name = reverse_geocode(lat, lon)

        # Reverse geocode "To" location
        if self.destination_location and not self.destination_location_name:
            lat, lon = map(float, self.destination_location.split(','))
            self.destination_location_name = reverse_geocode(lat, lon)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Trip from {self.from_location} to {self.destination_location} - {self.userid.name}"


class Review(models.Model):
    user = models.ForeignKey(tblUserReg, on_delete=models.CASCADE)  # Use tblUserReg instead of User
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 rating
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.vehicle.name} ({self.rating}⭐)"
