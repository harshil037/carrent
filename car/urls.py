from django.urls import path
from car import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("team", views.team, name='team'),
    path("faq", views.faq, name='faq'),
    path("fleet", views.fleet, name='fleet'),
    path("offers", views.offers, name='offers'),
    path("terms", views.terms, name='terms'),
    path("testimonials", views.testimonials, name='testimonials'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="profile"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("contact", views.contact , name="contact"),
    path("book", views.book, name="book"),
    path("book/<int:modelId>", views.book, name="book"),
    path("bookingdetails", views.bookingdetails, name="bookingdetails"),
    path("userbookings", views.userbookings, name="userbookings"),
    path("bookingdetails/[<modelId>,<bookingId>]", views.bookingdetails, name="bookingdetails"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)