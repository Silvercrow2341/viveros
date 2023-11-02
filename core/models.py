from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #mostrar los usuarios
from ckeditor.fields import RichTextField
# Create your models here.
class empresa(models.Model):
    titulo = models.CharField (max_length=70)
    image=models.ImageField(null=True, verbose_name='Imagen',upload_to='empresas')
    contenido = RichTextField ()
    creado = models.DateTimeField (auto_now_add=True) # añade la fecha automaticamente
    actualizado = models.DateTimeField (auto_now=True) # actualiza la fecha automaticamente

    class Meta:
        verbose_name = 'valor'
        verbose_name_plural = 'valores'
        ordering = ['-creado'] #sirve para ordenar del nuevo al antiguo

    def __str__(self): #cambiar el nombre del proyecto
        return self.titulo
    
    
class categoria(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now = True )

    class Meta:
        verbose_name = " Categoria "
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class links(models.Model):
    titulo = models.CharField (max_length=70)
    icono = models.CharField (max_length=70, blank=True)
    link_redes=models.URLField (null=True,blank=True)
    creado = models.DateTimeField (auto_now_add=True) # añade la fecha automaticamente
    actualizado = models.DateTimeField (auto_now=True) # actualiza la fecha automaticamente
    publicado = models.DateTimeField (default=now, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(categoria, related_name="get_posts")

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'
        ordering = ['-creado'] #sirve para ordenar del nuevo al antiguo

    def __str__(self): #cambiar el nombre del proyecto
        return self.titulo
    
