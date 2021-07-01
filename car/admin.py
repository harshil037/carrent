from django.contrib import admin
from car.models import Contact , Fleet

# Register your models here.

def getConatactModel(model):
    return [field.name for field in model._meta.get_fields()]

class ContactDetail(admin.ModelAdmin):
    list_display = getConatactModel(Contact)


def getFleetModel(model):
    return [field.name for field in model._meta.get_fields()]

class FleetDetail(admin.ModelAdmin):
    list_display = getFleetModel(Fleet)






admin.site.register(Contact, ContactDetail)

admin.site.register(Fleet, FleetDetail)
    

