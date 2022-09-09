from django.contrib import admin
from .models import Proveedor, Cuenta, Compra, Cliente, Venta
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Cuenta)
admin.site.register(Compra)
admin.site.register(Cliente)
admin.site.register(Venta)