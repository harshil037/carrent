from django.db.models import fields
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
        fields = '__all__'

class DateTimeInput(forms.DateInput):
    input_type = 'datetime'

class BookingForm(ModelForm):
    depositAmount = forms.DecimalField(disabled=True)
    securityProof = forms.CharField(required=True, label='Aadhar Number')
    pickupDate = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    class Meta:
        model = Booking
        fields = ("securityProof", "pickupDate", "dropDate")
        # widgets = {
        #     'pickupDate' : DateTimeInput(),
        # }