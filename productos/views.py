from django.shortcuts import render
from core.models import links
from productos.models import category
from productos.models import productos


# Create your views here.
def producto(request):
    link=links.objects.all()
    categoria=category.objects.all()
    product=productos.objects.all()
    return render (request, "productos/productos.html",{'link':link,'categoria':categoria, 'product':product})


