from django import forms
from django.contrib.messages.api import error
from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Booking, Contact, Fleet, Testimonials, CarModel
from .forms import ContactForm, NewUserForm, UserUpdateForm, BookingForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse, request
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


def index(request):
    # Limit number of cars on index page
    cars = CarModel.objects.all()[:3]
    testimonials = Testimonials.objects.all()[:2]
    return render(request, 'index.html', {'cars':cars, 'testimonials':testimonials})


def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def faq(request):
    return render(request, 'faq.html')


def fleet(request):
    return render(request, 'fleet.html')


def offers(request):
    return render(request, 'offers.html')


def terms(request):
    return render(request, 'terms.html')



def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("index")
        messages.error(
            request, "Unsuccessful registration. Invalid Information.")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.",)
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Car Rental Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('profile')
        else:
            messages.success(request,'There was an error! Please try again later.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context={'u_form': u_form}
    return render(request, 'user/profile.html',context )
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact information and message was successfully submitted.")
            return redirect("contact")
        else:
            message.error(request,"There was an error submitting your query. Please try again later.")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
    return redirect("/#footerform")

def fleet(request):
    cars = CarModel.objects.all()
    return render(request,"fleet.html",{'cars':cars})

def testimonials(request):
    feeds = Testimonials.objects.all()
    return render(request,"testimonials.html",{'feeds':feeds})

@login_required(login_url='login')
def book(request, modelId = 4):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            modelId = form.cleaned_data['modelId']
            bookingId = form.save()
            messages.success(request, "Success.")
            return redirect("bookingdetails",modelId=modelId,bookingId = bookingId.pk)
        else:
            messages.error(request, "Error")
        
    form = BookingForm(initial={'userId':request.user, 'modelId': modelId})
    context = {'form': form}
    return render(request, 'booking/book.html', context)

@login_required(login_url='login')
def bookingdetails(request, modelId, bookingId):
    book1 = Booking.objects.get(pk = bookingId)
    s_date = getattr(book1, 'pickupDate')
    e_date = getattr(book1, 'dropDate')
    date_format = "%Y-%m-%d"
    a = datetime.strptime(str(s_date), date_format)
    b = datetime.strptime(str(e_date), date_format)
    delta = b - a
    days = delta.days
    # car1 = Fleet.objects.filter(pk = book1.carId)
    modelId = modelId
    modelObj = CarModel.objects.get(modelName = modelId)
    price = getattr(modelObj, 'price')
    modelName = getattr(modelObj, 'modelName')
    grossamt = price * days
    totalamt = grossamt + 2499
    if Fleet.objects.filter(modelId = modelObj.pk, status= 0).exists() :
        carObj = Fleet.objects.get(modelId = modelObj.pk, status= 0)
        book1.carId = carObj
        carObj.status = 1
        carObj.save()
        book1.grossAmount = grossamt
        book1.totalAmount =  totalamt
        book1.save()
    else:
        messages.error(request, "Selected car not available at the moment. Please try again later or choose another car")
        return redirect('book/4')
    return render(request, "booking/bookingdetails.html",{'bookingId':bookingId,'price':price,'grossamt':grossamt, 'totalamt':totalamt, 'days':days, 'modelName': modelName,'s_date':s_date,'e_date':e_date})