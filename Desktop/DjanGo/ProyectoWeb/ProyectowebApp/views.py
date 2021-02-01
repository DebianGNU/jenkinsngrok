from django.shortcuts import render, HttpResponse

#Quedamos con el video 29 para verificar como lo hace el ya que no funciona de la forma que lo hago...

def home(request):  # home sigue siendo Home

    return render(request, "ProyectowebApp/home.html")

def servicios(request):

    return render(request, "ProyectowebApp/servicios.html")

def portafolio(request):  # tienda es reeplazado por portafolio

    return render(request, "ProyectowebApp/Portafolio.html")

def acerca_de(request):# Blog es reemplazado por acerca_de

    return render(request, "ProyectowebApp/Acerca_de.html")

def equipo(request):

    return render(request, "ProyectowebApp/Equipo.html")

def contacto(request):  # contacto sigue siendo contacto

    return render(request, "ProyectowebApp/contacto.html")
