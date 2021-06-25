from django.shortcuts import render


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

# contact pending