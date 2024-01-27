from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("appointment",views.appointment,name='appointment'),
    path("call",views.call,name='call'),
    path("classes",views.classes,name='classes'),
    path("contact",views.contact,name='contact'),
    path("facility",views.facility,name='facility'),
    path("team",views.team,name='team'),
    path("testimonial",views.testimonial,name='testimonial'),
    path("error",views.error,name='error')
]