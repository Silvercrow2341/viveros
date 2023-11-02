"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core import views as core_views
from django.conf import settings
from productos import views as productos_views
from portafolio import views as portafolio_views


from contacto import views as contacto_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home, name="inicio"),
    path('productos/',productos_views.producto, name="productos"),
    path('portafolio/',portafolio_views.portafolio, name="portafolio"),  
    path('contacto/',include('contacto.urls')),
    path('carro/', include('carro.urls')),
    path('pedidos/',include('pedidos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    #path('base/',core_views.urls, name="base"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
    
    # custom del admin

admin.site.site_header = "vivero los ocobos"
admin.site.index_title = "panel de administrador"
admin.site.site_title = "vivero ocobos"