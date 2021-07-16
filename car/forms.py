from django.db.models import fields, query
from django.db.models.enums import Choices
from django.forms import widgets
from car.models import Booking, CarModel, Contact, Fleet, Testimonials
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

class BookingForm(ModelForm):
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
    modelId = forms.ModelChoiceField(queryset=CarModel.objects.all(), label='Car' )
    securityProof = forms.CharField(required=True, label='Aadhar Number ', widget=forms.TextInput(attrs={'onblur': 'AadharValidation();'}))
    pickupDate = forms.DateField(label='Pickup Date ', widget=forms.DateInput(attrs={'type':'date'}))
    dropDate = forms.DateField(label='Drop Date ', widget=forms.DateInput(attrs={'type':'date'}))
    pickupLocation = forms.ChoiceField(label='Pickup Location ', choices=LOCATION_CHOICES)
    dropLocation = forms.ChoiceField(label='Drop Location ', choices=LOCATION_CHOICES)
    userId = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    # carId = forms.ModelChoiceField(queryset=Fleet.objects.all()[:1], widget=forms.HiddenInput())
    class Meta:
        model = Booking
        fields = ('modelId', 'pickupLocation', 'pickupDate', 'dropLocation', 'dropDate', 'userId')
        # widgets = {
        #     'pickupDate' : DateTimeInput(),
        # }

class GiveTestimonialForm(forms.ModelForm):
    username = forms.ModelChoiceField(queryset=User.objects.all(), widget= forms.HiddenInput())
    class Meta:
        model = Testimonials
        fields = ['name','notes']
    