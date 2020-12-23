from django.contrib import admin
from .models import Groups, Prod

# Register your models here.

class ProdAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'group',
        'name',
        'description',
        'price',
        'image',
        'offer',
    )


admin.site.register(Groups)
admin.site.register(Prod, ProdAdmin)
