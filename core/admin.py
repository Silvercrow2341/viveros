from django.contrib import admin
from .models import links
from .models import categoria
from .models import empresa





# Register your models here.

class linksAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class empresaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')



admin.site.register(links,linksAdmin)
admin.site.register(categoria,categoriaAdmin)
admin.site.register(empresa,empresaAdmin)
