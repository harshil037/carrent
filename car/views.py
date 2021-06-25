from typing import NewType
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

def testimonials(request):
    return render(request, 'testimonials.html')

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("index")
        messages.error(request,"Unsuccessful registration. Invalid Information.")
    form = NewUserForm
    return render (request=request, template_name="register.html", context={"register_form":form})

# contact pending