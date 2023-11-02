from django.contrib import admin
from .models import category,productos

class ProjectAdmin(admin.ModelAdmin): 
    readonly_fields=('created','updated')
    
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


admin.site.register(category,CategoryAdmin)
admin.site.register(productos,ProjectAdmin)