from django.urls import path
from car import views


urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("team", views.team, name='team'),
    path("faq", views.faq, name='faq'),
    path("fleet", views.fleet, name='fleet'),
    path("offers", views.offers, name='offers'),
    path("terms", views.terms, name='terms'),
    path("testimonials", views.testimonials, name='testimonials'),

    #contact pandenig
]