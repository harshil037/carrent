from django.urls import path
from car import views

urlpatterns = [
    path("", views.index, name='car'),
]