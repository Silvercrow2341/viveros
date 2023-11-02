from django.contrib import admin
from .models import profile

# Register your models here.
class profileadmin(admin.ModelAdmin):
    list_display = ('user', 'user_group')
    search_fields = ('user_username','user_groups_name')
    list_filter = ('user_groups')

    def user_group(self,obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = 'Grupo'


admin.site.register(profile)
