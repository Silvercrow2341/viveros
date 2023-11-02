from django.shortcuts import render,HttpResponse
from .models import links
from .models import empresa
from carro.carro import Carro

# Create your views here.


def home(request):
    empresas=empresa.objects.all()
    link=links.objects.all()
    carro = Carro(request)
    return render (request, "core/home.html", {'empresas':empresas,'link':link })

def contacto(request):
    link=links.objects.all()
    return render (request, "core/contacto.html", {'link':link })
