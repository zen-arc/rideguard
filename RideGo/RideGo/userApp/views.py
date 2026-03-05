from django.shortcuts import render, redirect, get_object_or_404

from indexapp.models import Driver, tblUserReg ,tblUserLog
from adminApp.models import Category
from driverApp.models import Vehicle

from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
import requests
from .forms import* 

import requests
import time

def user_index(request):
    drivers = Driver.objects.filter(status='approved')  # Filter drivers with status 'approved'
    vehicles = Vehicle.objects.all()    
    reviews = Review.objects.all()
    return render(request, 'user_index.html', {'drivers': drivers, 'vehicles': vehicles, 'reviews': reviews})



def view_drivers(request):
    drivers = Driver.objects.all()
    return render (request,'view_drivers.html',{'drivers':drivers}) 

def view_vehicles(request):

    vehicles = Vehicle.objects.all()

    # Retrieve filter values from the GET request
    model = request.GET.get('model')
    fuel_type = request.GET.get('fuel_type')
    no_of_seats = request.GET.get('no_of_seats')
    category = request.GET.get('category')

    # Apply filters if selected
    if model:
        vehicles = vehicles.filter(model=model)
    if fuel_type:
        vehicles = vehicles.filter(fuel_type=fuel_type)
    if no_of_seats:
        vehicles = vehicles.filter(no_of_seats=no_of_seats)
    if category:
        vehicles = vehicles.filter(category__id=category)  # Filter by category ID

    # Get distinct options dynamically from database
    distinct_models = Vehicle.objects.values_list('model', flat=True).distinct()
    distinct_fuel_types = Vehicle.objects.values_list('fuel_type', flat=True).distinct()
    distinct_seat_counts = Vehicle.objects.values_list('no_of_seats', flat=True).distinct()
    categories = Category.objects.all()  # Get all categories

    context = {
        'vehicles': vehicles,
        'models': distinct_models,
        'fuel_types': distinct_fuel_types,
        'seat_counts': distinct_seat_counts,
        'categories': categories,
    }
    
    return render(request, 'view_vehicles.html', context)
    
def vehicle_detail(request, pk):
    """View to display the details of a single product along with reviews."""
    vehicle = get_object_or_404(Vehicle, id=pk)
    reviews = Review.objects.filter(vehicle=vehicle).order_by('-created_at')  # Order by latest first
    
    return render(request, 'vehicle_detail.html', {
        'vehicle': vehicle,
        'reviews': reviews
    })

# def product_detail(request, pk):
#     vehicle = get_object_or_404(Vehicle, pk=pk)
#     return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    vehicles = Vehicle.objects.filter(driverid=driver)  # Fetch cars assigned to this driver
    return render(request, 'driver_detail.html', {'driver': driver, 'vehicles': vehicles})


# def trip_booking(request, vehicle_id):
#     if 'registration_id' not in request.session:
#         return redirect('userlog')  # Redirect if not logged in

#     user_id = request.session.get('registration_id')
#     user = tblUserReg.objects.get(id=user_id)
#     vehicle = Vehicle.objects.get(id=vehicle_id)

#     if request.method == "POST":
#         from_location = request.POST.get('from_location')
#         to_location = request.POST.get('to_location')
#         travel_date = request.POST.get('travel_date')
#         travel_time = request.POST.get('travel_time')

#         try:
#             # Check if vehicle is already booked for this date and time
#             if Booking.objects.filter(
#                 vehicleid=vehicle,
#                 travel_date=travel_date,
#                 travel_time=travel_time
#             ).exists():
#                 messages.error(request, "This vehicle is already booked for the selected date and time. Please choose a different time.")
#                 return redirect('trip_booking', vehicle_id=vehicle_id)

#             # Create the booking
#             booking = Booking.objects.create(
#                 userid=user,
#                 vehicleid=vehicle,
#                 driverid=vehicle.driverid,
#                 from_location=from_location,
#                 destination_location=to_location,
#                 travel_date=travel_date,
#                 travel_time=travel_time,
#                 total_price=vehicle.price_per_km
#             )
#             messages.success(request, "Booking successful!")
#             return redirect('my_bookings')  # Redirect to bookings page

#         except ValidationError as e:
#             messages.error(request, str(e))
#             return redirect('trip_booking', vehicle_id=vehicle_id)

#     return render(request, 'trip_booking.html', {
#         'user': user,
#         'vehicle': vehicle,
#     })


def geocode_location(location):
    """
    Geocode a location (address) to latitude and longitude using Photon.
    """
    url = f"https://photon.komoot.io/api/?q={location}"
    try:
        response = requests.get(url)
        print("Photon Response:", response.text)  # Log the raw response
        data = response.json()
        if data['features']:
            # Return the first result's latitude and longitude
            return float(data['features'][0]['geometry']['coordinates'][1]), float(data['features'][0]['geometry']['coordinates'][0])
        else:
            raise ValidationError(f"Could not geocode location: {location}")
    except Exception as e:
        raise ValidationError(f"Error geocoding location: {str(e)}")

def calculate_distance_osrm(from_location, to_location):
    """
    Calculate the distance between two locations using OSRM.
    Returns the distance in kilometers.
    """
    try:
        # Check if the input is already in latitude,longitude format
        def is_coordinate(location):
            try:
                lat, lon = map(float, location.split(','))
                return True
            except:
                return False

        # If the input is already coordinates, use them directly
        if is_coordinate(from_location) and is_coordinate(to_location):
            from_lat, from_lon = map(float, from_location.split(','))
            to_lat, to_lon = map(float, to_location.split(','))
        else:
            # Otherwise, geocode the locations
            from_lat, from_lon = geocode_location(from_location)
            to_lat, to_lon = geocode_location(to_location)

        # Use OSRM to calculate the distance
        osrm_url = f"http://router.project-osrm.org/route/v1/driving/{from_lon},{from_lat};{to_lon},{to_lat}?overview=false"
        response = requests.get(osrm_url).json()

        if response['code'] == 'Ok':
            # Extract distance in meters and convert to kilometers
            distance = response['routes'][0]['distance'] / 1000
            return distance
        else:
            raise ValidationError("Unable to calculate distance. Please check the locations.")
    except Exception as e:
        raise ValidationError(f"Error calculating distance: {str(e)}")
def trip_booking(request, vehicle_id):
    if 'registration_id' not in request.session:
        return redirect('userlog')  # Redirect if not logged in

    user_id = request.session.get('registration_id')
    user = tblUserReg.objects.get(id=user_id)
    vehicle = Vehicle.objects.get(id=vehicle_id)

    if request.method == "POST":
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        travel_date = request.POST.get('travel_date')
        travel_time = request.POST.get('travel_time')

        try:
            # Check if vehicle is already booked for this date and time
            if Booking.objects.filter(
                vehicleid=vehicle,
                travel_date=travel_date,
                travel_time=travel_time
            ).exists():
                messages.error(request, "This vehicle is already booked for the selected date and time. Please choose a different time.")
                return redirect('trip_booking', vehicle_id=vehicle_id)

            # Calculate distance between "From" and "To" locations using OSRM
            distance = calculate_distance_osrm(from_location, to_location)

            # Calculate total price based on distance and vehicle's price_per_km
            total_price = distance * vehicle.price_per_km

            # Create the booking
            booking = Booking.objects.create(
                userid=user,
                vehicleid=vehicle,
                driverid=vehicle.driverid,
                from_location=from_location,
                destination_location=to_location,
                travel_date=travel_date,
                travel_time=travel_time,
                total_price=total_price
            )
            messages.success(request, f"Booking successful! Total price: ₹{total_price:.2f}")
            return redirect('my_bookings')  # Redirect to bookings page

        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('trip_booking', vehicle_id=vehicle_id)
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('trip_booking', vehicle_id=vehicle_id)

    return render(request, 'trip_booking.html', {
        'user': user,
        'vehicle': vehicle,
    })
def my_bookings(request):
    user_id = request.session.get('registration_id')  # Get user ID from session
    if not user_id:
        return redirect('userlog')  # Handle missing session case
    
    booking = Booking.objects.filter(userid=user_id, status__in=['pending', 'available', 'not available', 'completed']).order_by('-id')
    
    return render(request, 'my_booking.html', {'booking': booking})


def reverse_geocode(lat, lon):
    """
    Reverse geocode latitude and longitude to a location name using Nominatim.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {
        "User-Agent": "YourAppName/1.0 (your@email.com)"  # Set a custom User-Agent
    }
    try:
        time.sleep(1)  # Respect Nominatim's rate limit
        response = requests.get(url, headers=headers)
        print("Nominatim Reverse Geocode Response:", response.text)  # Log the raw response
        data = response.json()
        if data and 'display_name' in data:
            return data['display_name']  # Return the location name
        else:
            return f"{lat}, {lon}"  # Fallback to coordinates if no name is found
    except Exception as e:
        print(f"Error reverse geocoding: {str(e)}")
        return f"{lat}, {lon}"  # Fallback to coordinates on error
def cancel_booking(request, id):
    Booking.objects.filter(id=id).update(status="cancelled")
    Booking.objects.filter(id=id).update(payment_status="cancelled")    
    messages.success(request, 'Booking cancelled successfully!')
    return redirect('my_bookings')


def add_review(request, vehicle_id):
    """Allow users to submit a review for a delivered product."""
    
    if not request.session.get('registration_id'):  # Ensure user is logged in
        messages.error(request, "You need to log in first.")
        return redirect('userlog')

    user_id = request.session['registration_id']
    user = get_object_or_404(tblUserReg, id=user_id)  # Get logged-in user
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.vehicle = vehicle
            review.user = user  # Assign logged-in user
            review.save()
            messages.success(request, "Your review has been submitted successfully!")
            return redirect('my_bookings')  # Redirect back to orders page
        else:
            return render(request, 'add_review.html', {'form': form, 'vehicle': vehicle, 'show_alert': True,
                    'sweetalert': {
                        'icon': 'error',
                        'title': 'Not Added!',
                        'text': 'Please select the rating!',    
                    }})                            
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'vehicle': vehicle})

def admin_booking_list(request):
    book = Booking.objects.filter(payment_status='paid')
    if not book:
        print('No bookings available.')
    print(book)  # Debugging print statement    
    return render(request, 'admin_booking_list.html', {'bookings': book})

import re

def edit_profile(request):
    user_id = request.session.get('registration_id')
    if not user_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('userlog')  # replace 'login' with your login route name

    try:
        userreg = tblUserReg.objects.get(id=user_id)
        userlogs = tblUserLog.objects.get(id=userreg.login_id)
    except (tblUserReg.DoesNotExist, tblUserLog.DoesNotExist):
        messages.error(request, "User not found.")
        return redirect('userlog')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Validations
        if not name or not phone or not email or not password:
            messages.error(request, "All fields are required.")
        elif not re.fullmatch(r"[A-Za-z ]{3,100}", name):
            messages.error(request, "Name must be 3-100 characters and contain only letters and spaces.")


        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
        elif not re.search(r"[A-Za-z]", password):
            messages.error(request, "Password must contain at least one letter.")
        elif not re.search(r"\d", password):
            messages.error(request, "Password must contain at least one number.")
        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.error(request, "Password must contain at least one special character.")
        else:
            # Save updates
            userreg.name = name
            userreg.phone_number = phone
            userlogs.email = email
            userlogs.password = password  # You can hash it if needed
            userreg.country = country
            userreg.save()
            userlogs.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')  # redirect to avoid resubmission

    return render(request, 'edit_profile.html', {'userreg': userreg, 'userlog': userlogs})
