from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Size)
admin.site.register(Piping)
admin.site.register(Material)
admin.site.register(AccessoriesSize)
#admin.site.register(Pipes)
admin.site.register(AccessoriesType)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['active']


admin.site.register(Accessories,AccessoriesAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = ['pipes_price','size','material','piping']
    list_filter = ['active']


admin.site.register(Price, PriceAdmin)


class AccessoriesPriceAdmin(admin.ModelAdmin):
    list_display = ['accessories_price', 'name', 'size', 'type']
    list_filter = ['active']


admin.site.register(AccessoriesPrice, AccessoriesPriceAdmin)
