from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings
from django.core.mail import send_mail


from .models import tblUserLog
from django.contrib import messages

from indexapp.forms import* 
from driverApp.models import Vehicle
from userApp.models import Review
def index(request):
    drivers = Driver.objects.filter(status='approved')  # Filter drivers with status 'approved'
    vehicles = Vehicle.objects.all()    
    reviews = Review.objects.all()
    return render(request, 'index.html', {'drivers': drivers, 'vehicles': vehicles, 'reviews': reviews})





def userlog(request):
    if request.method == "GET":
        form = loginForms()
        return render(request, 'userlog.html', {'form': form}) 

    else:
        form = loginForms()    
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            userdetail = tblUserLog.objects.get(email=email, password=password)
            request.session['login_id'] = userdetail.id  # Store login ID in session
            
            if userdetail.usertype == 'admin':
                return redirect('adminhome')
            
            elif userdetail.usertype == 'driver':
                driver = Driver.objects.get(loginid_id=userdetail.id)  # Ensure correct field

                if driver:
                    request.session['driver_id'] = driver.id
                    print(request.session.get('driver_id'))
                    
                if driver.status == 'pending':
                    messages.info(request, "Your account is pending approval.")
                    return redirect('userlog')
                else:
                    messages.success(request, "Login successful!")
                    return redirect('driver_home')

            elif userdetail.usertype == 'user':
                reg_details = tblUserReg.objects.get(login_id=userdetail.id)  # Ensure correct field
                
                if reg_details:
                    request.session['registration_id'] = reg_details.id
                    print(request.session.get('registration_id'))  
                    return redirect('user_index')

        except tblUserLog.DoesNotExist:
            print("Invalid login attempt")
            messages.error(request, "Invalid credentials.")  # Display error message

        return render(request, 'userlog.html', {'form': form})



def userreg(request):
    if request.method == "GET":
        form = UserRegForm()
        return render(request, 'userreg.html', {'form': form}) 
    else:
        if request.method == "POST":
            form = UserRegForm(request.POST)
            print(form.errors)  # Debug: Print form errors to check for validation issues
            if form.is_valid():
                print("Form is valid")  # Optional debug message

                # Extract cleaned data
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data.get('first_name', 'Customer')  # Get first name if available

                # Create and save a login object
                login_data = tblUserLog(email=email, password=password, usertype="user")
                login_data.save()

                # Get the last inserted ID (primary key of the login instance)
                last_inserted_id = login_data.id

                # Save the CustomerRegForm instance, associating it with the login instance
                obj = form.save(commit=False)
                obj.login_id = last_inserted_id  
                obj.save()

                # **Send Welcome Email**
                subject = "Welcome to Our Platform!"
                message = f"""
                Dear {first_name},\n\n
                Thank you for registering with us.
                Your account has been successfully created.
                
                You can now log in using the email: {email}
                
                Best regards,
                Your Website Team
                """
                from_email = f"RideGo <{settings.EMAIL_HOST_USER}>"  # Custom sender name
                recipient_list = [email]

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                messages.success(request, "Registration successful! A welcome email has been sent.")
                return redirect('userlog')

            else:
                messages.error(request, "Registration failed. Please check your details.")
                return render(request, 'userreg.html', {'form': form})

# def userreg(request):
    
#     if request.method=="GET":
#         form=UserRegForm()
#         return render(request,'userreg.html',{'form':form}) 
#     else:
#         if request.method == "POST":
#                 form = UserRegForm(request.POST)
#                 print(form.errors)  # Debug: Print form errors to check for validation issues
#                 if form.is_valid():
#                     print("Form is valid")  # Optional debug message

#                     # Extract cleaned data
#                     email = form.cleaned_data['email']
#                     password = form.cleaned_data['password']

#                     # Create and save a login object
#                     login_data = tblUserLog(email=email, password=password, usertype="user")
#                     login_data.save()

#                     # Get the last inserted ID (primary key of the login instance)
#                     last_inserted_id = login_data.id

#                     # Save the CustomerRegForm instance, associating it with the login instance
#                     obj = form.save(commit=False)
#                     obj.login_id = last_inserted_id  # Assuming the related field in your Customer model is login_id
#                     obj.save()

                  
                 
#                     message="This is a success message!"
#                     return redirect('userlog')
#                 else:
#                     message="This is unsuccessful message!"
#                     return render(request,'userreg.html',{'form':form})
                
                
def driver_reg(request):   
    if request.method=="GET":
        form=DriverRegForm()
        return render(request,'driver_reg.html',{'form':form}) 
    else:
        if request.method == "POST":
                form = DriverRegForm(request.POST,request.FILES)
                print(form.errors)  # Debug: Print form errors to check for validation issues
                if form.is_valid():
                    print("Form is valid")  # Optional debug message

                    # Extract cleaned data
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']

                    # Create and save a login object
                    login_data = tblUserLog(email=email, password=password, usertype="driver")
                    login_data.save()
                    print(form.errors)  # Debug: Print form errors to check for validation issues

                    # Get the last inserted ID (primary key of the login instance)
                    last_inserted_id = login_data.id

                    # Save the CustomerRegForm instance, associating it with the login instance
                    obj = form.save(commit=False)
                    obj.loginid_id = last_inserted_id  # Assuming the related field in your Customer model is login_id
                    obj.save()

                  
                 
                    message="This is a success message!"
                    return redirect('userlog')
                else:
                    message="This is unsuccess message!"
                    return render(request,'driver_reg.html',{'form':form})     
                
                
