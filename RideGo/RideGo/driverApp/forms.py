from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Vehicle

from indexapp.models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['loginid', 'status']  # Optional: adjust as needed



class VehicleForm(forms.ModelForm):
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('CNG', 'CNG'),
    ]

    fuel_type = forms.ChoiceField(
        choices=FUEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Vehicle
        exclude = ['driverid']
        fields = [
            'name',
            'image',
            'regno',
            'category',
            'fuel_type',
            'model',
            'no_of_seats',
            'price_per_km',
        ]

        labels = {
            'name': 'Name',
            'image': 'Image',
            'regno': 'Registration Number',
            'category': 'Category',
            'fuel_type': 'Fuel Type',
            'model': 'Model',
            'no_of_seats': 'Number of Seats',
            'price_per_km': 'Price Per Kilometer',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Vehicle Name', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'regno': forms.TextInput(attrs={'placeholder': 'Enter Registration Number', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'placeholder': 'Enter Model', 'class': 'form-control'}),
            'no_of_seats': forms.NumberInput(attrs={'placeholder': 'Enter Number of Seats', 'class': 'form-control'}),
            'price_per_km': forms.NumberInput(attrs={'placeholder': 'Enter Price Per Kilometer', 'class': 'form-control'}),
        }

    def clean_regno(self):
        regno = self.cleaned_data.get('regno')
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
        if not re.match(pattern, regno):
            raise ValidationError("Invalid registration number! Example format: KL17G5462")
        return regno
