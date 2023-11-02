from django.db import models
from django.utils.timezone import now

class category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    created = models.DateTimeField(auto_now=True,verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")
    
    class meta: 
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=["-created"]
    def __str__(self):
        return self.name
    
class productos(models.Model):
    title=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.TextField(verbose_name='Descripcion')
    image=models.ImageField(verbose_name='Imagen',upload_to='projects')
    categories=models.ManyToManyField(category,max_length=20, verbose_name="categoria")
    price=models.FloatField(max_length=20,verbose_name="Precio")
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creacion') #añade de forma automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")
    

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        ordering=["-created"] #ordena del nuevo al antiguo

    def __str__(self):
        return self.title