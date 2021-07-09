from django.db.models import fields
from django.db.models.enums import Choices
from django.forms import widgets
from car.models import Booking, Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'notes']

class DateTimeInput(forms.DateInput):
    input_type = 'datetime'

class BookingForm(ModelForm):
    LOCATION_CHOICES = [
        ('Ahmedabad',(
            ('ahmrailway','Railway Station'),
            ('ahmairport','Ahmedabad Airport')
        ))
    ]
    depositAmount = forms.DecimalField(label='Deposit Amount ₹', initial=2499 ,disabled=True)
    securityProof = forms.CharField(required=True, label='Aadhar Number ', widget=forms.TextInput(attrs={'onblur': 'AadharValidation();'}))
    pickupDate = forms.DateTimeField(label='Pickup Date ')
    dropDate = forms.DateTimeField(label='Drop Date ')
    pickupLocation = forms.ChoiceField(label='Pickup Location ', choices=LOCATION_CHOICES)
    dropLocation = forms.ChoiceField(label='Drop Location ', choices=LOCATION_CHOICES)
    # userId = forms.
    class Meta:
        model = Booking
        fields = ('pickupLocation', 'pickupDate', 'dropLocation', 'dropDate', 'depositAmount')
        # widgets = {
        #     'pickupDate' : DateTimeInput(),
        # }