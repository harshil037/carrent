from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    notes = models.TextField()

    def __str__(self):
        return self.name
class CarModel(models.Model):
    modelId = models.AutoField(primary_key=True)
    modelName = models.CharField(max_length=128, null=False, default='Maruti Suzuki Swift')
    modelYear = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
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
    name = models.CharField(max_length=128)
    notes = models.TextField(editable=False, null=False)
    rating = models.IntegerField(default= 5)

    def __str__(self):
        return self.name

class Booking(models.Model):
    securityProof = models.CharField(max_length=12,unique=True)
    depositAmount = models.DecimalField(max_digits=5, default=2499,decimal_places=2, editable=False)
    isDepositPaid = models.BooleanField()
    pickupDate = models.DateTimeField()
    dropDate = models.DateTimeField()
    bookingDate = models.DateField(auto_now_add='True')
    # pickupLocationId = models.IntegerField(ForeignKey = )
    # dropLocationId = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    # paymentId

