from django.contrib import admin
from django.db.models.base import Model
from car.models import CarModel, Contact , Fleet , Testimonials

# Register your models here.

def getContactModel(model):
    return [field.name for field in model._meta.get_fields()]

class ContactDetail(admin.ModelAdmin):
    list_display = getContactModel(Contact)

def getFleetModel(model):
    return [field.name for field in model._meta.get_fields()]

class FleetDetail(admin.ModelAdmin):
    list_display = getFleetModel(Fleet)

def getTestimonialModel(model):
    return [field.name for field in model._meta.get_fields()]

class TestimonialDetail(admin.ModelAdmin):
    list_display = getTestimonialModel(Testimonials)

admin.site.register(Contact, ContactDetail)
admin.site.register(Fleet, FleetDetail)
admin.site.register(Testimonials, TestimonialDetail)

def getCarModelModel(model):
    return [field.name for field in model._meta.get_fields()]

class CarModelDetail(admin.ModelAdmin):
    list_display=('modelId','modelName','modelYear','modelType', 'modelImg','price')
admin.site.register(CarModel, CarModelDetail)