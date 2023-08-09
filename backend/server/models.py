from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True) 
    contact = models.CharField(max_length=10, null=True) 
    address = models.CharField(max_length=250, null=True) 
    age = models.CharField(max_length=3, null=True) 
    createdAt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100, null=True) 
    contact = models.CharField(max_length=10, null=True) 

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    FULL_CAPACITY = (
        (True, 'True'),
        (False, 'False'),
    )

    veh_name = models.CharField(max_length=100, null=True) 
    veh_number = models.CharField(max_length=100, null=True) 
    veh_make = models.CharField(max_length=100, null=True)
    veh_location = models.CharField(max_length=100, null=True)  
    fullcapacity = models.BooleanField(null=True, choices=FULL_CAPACITY)

    def __str__(self):
        return self.veh_name

class Trip(models.Model):
    STATUS = (
        ('Arriving', 'Arriving'),
        ('Ongoing', 'Ongoing'),
        ('Complete', 'Complete'),
    )
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
    tripdate = models.CharField(max_length=100, null=True)
    triptype = models.CharField(max_length=100, null=True)
    pickupaddress = models.CharField(max_length=100, null=True)
    dropoffaddress = models.CharField(max_length=100, null=True)
    pickupgeocode = models.CharField(max_length=100, null=True)
    dropoffgeocode = models.CharField(max_length=100, null=True)
    pickuptime = models.TimeField(null=True)
    dropofftime = models.TimeField(null=True)
    stops = models.JSONField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    
    def __str__(self):
        return f'Trip#{self.id}'
