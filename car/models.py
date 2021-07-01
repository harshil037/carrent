from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    notes = models.TextField()

    def __str__(self):
        return self.name


class Fleet(models.Model):
    carType = models.CharField(max_length=128)
    plateNo = models.CharField(max_length=10)
    carImg = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    STATUS_CHOICES = [(0,'Available'),(1,'Booked'),(2,'Maintainance')]
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.carType

class Testimonials(models.Model):
    name = models.CharField(max_length=128)
    notes = models.TextField()
    rating = models.IntegerField(default= 0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    securityProof = models.CharField(max_length=12,unique=True)
    depositAmount = models.DecimalField(max_digits=5, default=2499,decimal_places=2)
    isDepositPaid = models.BooleanField()
    pickupDate = models.DateTimeField()
    dropDate = models.DateTimeField()
    bookingDate = models.DateField(auto_now_add='True')
    # pickupLocationId = models.IntegerField(ForeignKey = )
    # dropLocationId = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    # paymentId

