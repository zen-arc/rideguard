from django import forms
from .models import tblUserReg, tblUserLog, Driver


from django.core.exceptions import ValidationError
import re

class loginForms(forms.ModelForm):
    class Meta:
        model = tblUserLog
        fields = [
            'email',
            'password'
        ]
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email', 'class': 'form-group'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password','class': 'form-group'}),
        }
    def clean_email(self):
        """Validate email format and check existence."""
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email field cannot be empty.")
        if not tblUserLog.objects.filter(email=email).exists():
            raise ValidationError("No account found with this email.")
        return email

    def clean_password(self):
        """Check password length (minimum 8 characters)."""
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password        




class UserRegForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-group',
            'placeholder': 'Your Email'
        }),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-group',
            'placeholder': 'Password'
        }),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-group',
            'placeholder': 'Confirm Password'
        }),
        label="Confirm Password"
    )

    class Meta:
        model = tblUserReg
        fields = '__all__'
        exclude = ['login']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Your Name'
            }),
            
            'country': forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}),
            'phone_country_code': forms.TextInput(attrs={'placeholder': '+91', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            

        }
    def clean_name(self):
        """Ensure the name contains only letters and spaces."""
        name = self.cleaned_data.get("name")
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name
    
    def clean_email(self):
        """Check if email is unique."""
        email = self.cleaned_data.get("email")
        if tblUserLog.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        """Ensure password strength."""
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain both letters and numbers.")
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError("Password must contain at least one special character (@, $, !, %, *, ?, &).")
        return password


    

    def clean(self):
        """Check if passwords match."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data

 


class DriverRegForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = Driver
        fields = '__all__'
        exclude = ['loginid', 'status']
        labels = {
            'name': 'Name',
            'image': 'Image',
            'pcc': 'Police Clearance Certificate',
            'aadhar': 'Aadhar',
            'country': 'Country',
            'phone_country_code': 'Country Code',
            'phone_number': 'Phone Number',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pcc': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'aadhar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'license': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}),
            'phone_country_code': forms.TextInput(attrs={'placeholder': '+91', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        }



        
    def clean_name(self):
        """Ensure the name contains only letters and spaces."""
        name = self.cleaned_data.get("name")
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name
    
    def clean_email(self):
        """Check if email is unique."""
        email = self.cleaned_data.get("email")
        if tblUserLog.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
        
    def clean_password(self):
        """Ensure password strength."""
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain both letters and numbers.")
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError("Password must contain at least one special character (@, $, !, %, *, ?, &).")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data
 
 
