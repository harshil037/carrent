from django.contrib import admin
from django.db.models import fields
from django.db.models.base import Model
from car.models import CarModel, Contact , Fleet , Testimonials, Booking

# Register your models here.
def getBookingModel(model):
    return [field.name for field in model._meta.get_fields() ]
class BookingDetail(admin.ModelAdmin):
    list_display = getBookingModel(Booking)

def getContactModel(model):
    return [field.name for field in model._meta.get_fields()]
class ContactDetail(admin.ModelAdmin):
    list_display = getContactModel(Contact)
    readonly_fields = ['notes']

admin.site.register(Contact, ContactDetail)
admin.site.register(Booking, BookingDetail)

class CarModelDetail(admin.ModelAdmin):
    list_display=('modelId','modelName','modelType', 'modelImg','price')
admin.site.register(CarModel, CarModelDetail)

class FleetDetail(admin.ModelAdmin):
    list_display=('id', 'plateNo', 'modelId', 'status')
admin.site.register(Fleet, FleetDetail)

class TestimonialDetail(admin.ModelAdmin):
    list_display= ('id', 'name', 'notes')
admin.site.register(Testimonials, TestimonialDetail)