from .models import  Vehicle
from adminApp.models import Category
from indexapp.models import Driver,tblUserLog, tblUserReg
from userApp.models import Booking, Review

from .forms import VehicleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages





def driver_home(request):
    # Ensure driver is logged in via session
    driver = request.session.get('driver_id')
    if not driver:
        messages.error(request, "You need to log in first.")
        return redirect('login')
    
    driverbro = Driver.objects.get(id=driver)  # Fetch the logged-in driver

        
    return render(request, 'driver_home.html', {'driverbro': driverbro})




# Add Vehicles
def add_vehicle(request):
    vehicles = Vehicle.objects.filter(driverid=request.session.get('driver_id'))
    cat = Category.objects.all()
    driver = Driver.objects.get(id=request.session.get('driver_id'))
    print(driver)
    

    form = VehicleForm()

    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            driver = Driver.objects.get(id=request.session.get('driver_id'))
            form.driverid = driver
            form.save()
            messages.success(request, 'Vehicle added successfully!')
            return redirect('add_vehicle')
        else:
            messages.error(request, 'There was an error adding the vehicle.')

    return render(request, 'add_vehicle.html', {'form': form, 'vehicle':vehicles, 'cat': cat, 'dr':driver})

def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully!')
        else:
            messages.error(request, 'Error updating vehicle. Please check the registration number format.')

    return redirect('add_vehicle')

# Delete Vehicle
def del_vehicle(request, id):
    vehcle = get_object_or_404(Vehicle, id=id)
    vehcle.delete()
    messages.success(request, 'Vehicle deleted successfully!')
    return redirect('add_vehicle')



def booking_list(request):
    bookings = Booking.objects.filter(driverid=request.session.get('driver_id')).order_by('-created_at')
    return render(request, 'booking_list.html', {'booking': bookings})


def update_order_status(request, id):
    """Update the status of a booking, and set payment_status accordingly."""
    booking = get_object_or_404(Booking, id=id)

    if booking.status == "cancelled":
        messages.error(request, "Cancelled bookings cannot be updated.")
    elif request.method == 'POST':
        new_status = request.POST.get('status')
        booking.status = new_status

        # Set payment_status based on status
        if new_status == "completed":
            booking.payment_status = "paid"
        else:
            booking.payment_status = "unpaid"

        booking.save()
        messages.success(request, f"Booking {id} status updated to {new_status}.")
    
    return redirect('booking_list')



def reviews_list(request):
    """Display reviews for vehicles assigned to the logged-in driver, sorted by newest first."""

    # Ensure driver is logged in via session
    login_id = request.session.get('login_id')
    if not login_id:
        messages.error(request, "You need to log in first.")
        return redirect('login')

    try:
        driver = Driver.objects.get(loginid=login_id)  # Fetch the logged-in driver
    except Driver.DoesNotExist:
        messages.error(request, "Invalid driver account. Please log in again.")
        return redirect('login')

    # Fetch vehicles assigned to this driver
    vehicles = Vehicle.objects.filter(driverid=driver)

    # Fetch reviews for those vehicles
    reviews = Review.objects.filter(vehicle__in=vehicles).order_by('-created_at')

    return render(request, 'review.html', {'reviews': reviews})

def logout(request):
    """Logs out the user by clearing session data and redirecting to the index page."""
    request.session.flush()  # Clear all session variables
    return redirect('index')  # Redirect to the index page





from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators import gzip
from .drowsiness_detection import DrowsinessDetector
import threading

detector_instance = None
detector_thread = None

@gzip.gzip_page
def drowsiness_feed(request):
    global detector_instance
    try:
        if detector_instance is None:
            detector_instance = DrowsinessDetector()
        return StreamingHttpResponse(detector_instance.start_detection(),
                                  content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print("Video feed error:", str(e))
        return JsonResponse({'error': str(e)})

def start_drowsiness_detection(request):
    global detector_instance, detector_thread
    if request.method == 'POST':
        try:
            if detector_instance is None:
                detector_instance = DrowsinessDetector()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def stop_drowsiness_detection(request):
    global detector_instance
    if request.method == 'POST':
        try:
            if detector_instance is not None:
                detector_instance.stop_detection()
                detector_instance = None
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



import re


def edit_driver(request):
    user_id = request.session.get('driver_id')
    if not user_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('userlog')

    try:
        driver = Driver.objects.get(id=user_id)
    except (tblUserReg.DoesNotExist, tblUserLog.DoesNotExist, Driver.DoesNotExist):
        messages.error(request, "Driver data not found.")
        return redirect('userlog')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        phone_country_code = request.POST.get('phone_country_code', '').strip()

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


            # Update driver details
            driver.name = name
            driver.phone_number = phone
            driver.country = country
            driver.phone_country_code = phone_country_code
            driver.loginid.password = password  # Consider hashing here

            if 'image' in request.FILES:
                driver.image = request.FILES['image']
            if 'pcc' in request.FILES:
                driver.pcc = request.FILES['pcc']
            if 'aadhar' in request.FILES:
                driver.aadhar = request.FILES['aadhar']
            if 'license' in request.FILES:
                driver.license = request.FILES['license']

            driver.loginid.save()
            driver.save()

            messages.success(request, "Profile updated successfully!")
            return redirect('edit_driver')

    return render(request, 'edit_driver.html', {
        'driver': driver,
    })
