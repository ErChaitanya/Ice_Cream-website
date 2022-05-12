from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #agar kuch nahi hua toh home pr jayega
    path("", views.index, name='home'),
    #agar about hua toh about me jayega 
    path("about", views.about, name='about'),

    path("services", views.services, name='services'),

    path("contact", views.contact, name='contact'),
    # path("contact", views.contact, name='contact'),


    #view ke index function ko run karega jaise hi Httpresponse se request aayegi toh.

]
