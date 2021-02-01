from django.urls import path

from ProyectowebApp import views

urlpatterns = [
    path('home/',views.home, name="Home"),
    path('servicios/',views.servicios, name="Servicios"),
    path('portafolio/',views.portafolio, name="Portafolio"),
    path('acerca_de/',views.acerca_de, name="Acerca_de"),
    path('equipo/',views.equipo, name="Equipo"),
    path('contacto/',views.contacto, name="Contacto"),
]