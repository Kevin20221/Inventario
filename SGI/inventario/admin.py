from django.contrib import admin
from.models import producto
from.models import proveedor
from .models import factura
from .models import proveedora
# Register your models here.
admin.site.register(producto)
admin.site.register(proveedor)
admin.site.register(factura)
admin.site.register(proveedora)
