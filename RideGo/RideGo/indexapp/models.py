from django.db import models

# Create your models here.

class tblUserReg(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    country = models.CharField(null=True, blank=True, max_length=100)
    phone_country_code = models.CharField(null=True, blank=True, max_length=5)  # e.g., +91, +1
    login = models.ForeignKey('tblUserLog', on_delete=models.CASCADE)


class tblUserLog(models.Model):
    email = models.EmailField(max_length=50)  # Adjusted max_length to a more suitable size
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=20)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pcc = models.FileField(upload_to='documents/')
    aadhar = models.FileField(upload_to='documents/')
    license = models.FileField(null=True, blank=True, upload_to='documents/')

    country = models.CharField(null=True, blank=True, max_length=100)
    phone_country_code = models.CharField(null=True, blank=True, max_length=5)  # e.g., +91, +1
    phone_number = models.CharField(null=True, blank=True, max_length=150)

    loginid = models.ForeignKey(tblUserLog, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return self.name
    
    


