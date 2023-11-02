from django.shortcuts import render

from django.shortcuts import render

from .carro import Carro

from productos.models import productos

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, productos_id):

    carro = Carro(request)

    producto = productos.objects.get(id=productos_id)

    carro.agregar(productos=producto)

    return redirect("productos")

def eliminar_producto(request, productos_id):

    carro = Carro(request)

    producto = productos.objects.get(id=productos_id)

    carro.eliminar(productos=producto)

    return redirect("productos")

def restar_producto(request, productos_id):

    carro = Carro(request)

    producto = productos.objects.get(id=productos_id)

    carro.restar_producto(productos=producto)

    return redirect("productos")

def limpiar_carro(request, productos_id):

    carro = Carro(request)

    carro.limpiar_carro

    return redirect("productos")

# Create your views here.
