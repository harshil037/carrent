from django.contrib import admin
from car.models import Contact

# Register your models here.

def getConatactModel(model):
    return [field.name for field in model._meta.get_fields()]

class ContactDetail(admin.ModelAdmin):
    list_display = getConatactModel(Contact)

admin.site.register(Contact, ContactDetail)