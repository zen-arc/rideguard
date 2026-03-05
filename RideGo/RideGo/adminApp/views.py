from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import* 
from indexapp.models import Driver, tblUserLog, tblUserReg
from driverApp.models import Vehicle

from django.db.models import Sum, Count

def adminhome(request):
        
    return render(request, 'adminhome.html')



# # Create your views here.
# def adminhome(request):
#     return render(request, 'adminhome.html')

# Add or List Categories
def add_category(request):
    categories = Category.objects.all()
    form = AddCategoryForm()

    if request.method == "POST":
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('add_category')
        else:
            messages.error(request, 'There was an error adding the category.')

    return render(request, 'add_category.html', {'form': form, 'cat': categories})

# Edit Category
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
        else:
            messages.error(request, 'Error updating category.')

    return redirect('add_category')

# Delete Category
def del_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('add_category')




#approve function for company
def approve_driver(request,id):
    Driver.objects.filter(id=id).update(status="approved")
    obj=Driver.objects.all()

    return redirect('driver_Approved')

#delete function for company
def reject_driver(request,id):
    dr = Driver.objects.get(id=id).loginid_id
    print(dr)
    tblUserLog.objects.filter(id=dr).delete()
    
    obj = Driver.objects.all()
    return redirect('driver_Pending')






def driver_Approved(request):
    obj=Driver.objects.filter(status="approved")

    return render(request, 'driver_approved.html',{'com':obj})

def driver_Pending(request):
    obj=Driver.objects.filter(status="pending")

    return render(request, 'driver_pending.html',{'com':obj})



def view_vehicle(request):
    obj=Vehicle.objects.all()

    return render(request,'view_vehicle.html',{'vehicle':obj}) 




from django.db.models import Count
import json
from userApp.models import Booking  # Import the Booking model

def booking_status_report(request):
    # Query booking status count
    booking_data = (
        Booking.objects.values("status")
        .annotate(total_bookings=Count("id"))
        .order_by("status")
    )

    labels = [entry["status"] for entry in booking_data]
    data = [entry["total_bookings"] for entry in booking_data]

    context = {
        "labels": json.dumps(labels),  # Convert to JSON
        "data": json.dumps(data),      # Convert to JSON
        "total_bookings": sum(data)    # Total count
    }

    return render(request, "booking_status_report.html", context)


from django.db.models import Avg

def top_rated_vehicles_report(request):
    from userApp.models import Review, Vehicle
    top_vehicles = (
        Vehicle.objects.annotate(avg_rating=Avg("review__rating"))
        .order_by("-avg_rating")[:5]
    )

    labels = [vehicle.name for vehicle in top_vehicles]
    data = [vehicle.avg_rating for vehicle in top_vehicles]

    context = {
        "labels": json.dumps(labels),
        "data": json.dumps(data),
        "top_vehicles": top_vehicles
    }

    return render(request, "top_rated_vehicles_report.html", context)


def driver_availability_report(request):
    driver_data = (
        Driver.objects.values("status")
        .annotate(total_drivers=Count("id"))
        .order_by("status")
    )

    labels = [entry["status"] for entry in driver_data]
    data = [entry["total_drivers"] for entry in driver_data]

    context = {
        "labels": json.dumps(labels),
        "data": json.dumps(data),
        "total_drivers": sum(data)
    }

    return render(request, "driver_availability_report.html", context)



def category_wise_vehicle_report(request):
    category_data = (
        Vehicle.objects.values("category__name")
        .annotate(total_vehicles=Count("id"))
        .order_by("category__name")
    )

    labels = [entry["category__name"] for entry in category_data]
    data = [entry["total_vehicles"] for entry in category_data]

    context = {
        "labels": json.dumps(labels),
        "data": json.dumps(data),
        "total_vehicles": sum(data)
    }

    return render(request, "category_wise_vehicle_report.html", context)