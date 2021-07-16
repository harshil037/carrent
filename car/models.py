from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.exceptions import ValidationError
import datetime
from django_cryptography.fields import encrypt

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    notes = models.TextField()    
    isResolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class CarModel(models.Model):
    modelId = models.AutoField(primary_key=True)
    modelName = models.CharField(max_length=128, null=False, default='Maruti Suzuki Swift')
    # modelYear = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    MODELTYPE_CHOICES = [('Hatchback','Hatchback'), ('Sedan','Sedan'), ('SUV','SUV'), ('Luxury','Luxury')]
    modelType = models.CharField(max_length=128, choices = MODELTYPE_CHOICES, default=MODELTYPE_CHOICES[0])
    modelImg = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.modelName


class Fleet(models.Model):
    plateNo = models.CharField(max_length=10, null= False, unique=True)
    modelId = ForeignKey(CarModel, on_delete=models.CASCADE)
    STATUS_CHOICES = [(0,'Available'),(1,'Booked'),(2,'Maintainance')]
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.plateNo

class Testimonials(models.Model):
    name = models.CharField(max_length=512)
    notes = models.TextField(null=False)
    rating = models.IntegerField(editable=False, default= 5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Booking(models.Model):
    LOCATION_CHOICES = [
        ('Ahmedabad',(
            ('ahmrailway','Ahmedabad Railway Station'),
            ('ahmairport','Ahmedabad Airport')
        )),
        ('Mumbai',(
            ('mumrail', 'Mumbai Railway Statin'),
            ('mumairport', 'Mumbai Airport')
        ))
    ]
    securityProof = encrypt(models.CharField(max_length=256))
    # isDepositPaid = models.BooleanField(default=False)
    pickupDate = models.DateField()
    dropDate = models.DateField()
    pickupLocation = models.CharField(max_length=128, choices=LOCATION_CHOICES)
    dropLocation = models.CharField(max_length=128, choices=LOCATION_CHOICES)
    creationDate = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    totalAmount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    grossAmount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    carId = models.ForeignKey(Fleet, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [('saved', 'Saved'), ('paid', 'Paid'), ('done','Done')]
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    # paymentId
