from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render



class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):  # Nuestra primer vista...
    

    
    
    
    