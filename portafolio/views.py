from django.shortcuts import render
from core.models import links
from productos.models import category
from productos.models import productos
# from productos.models import producto, category

# Create your views here.
def portafolio(request):
    projects=productos.objects.all()
    link=links.objects.all()
    categoria=category.objects.all()
    return render (request, "portafolio/portafolio.html",{'projects':projects,'link':link,'categoria':categoria})