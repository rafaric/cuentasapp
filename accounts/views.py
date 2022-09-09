from pydoc import cli
from django.shortcuts import render
from django.views import View
from .models import Proveedor, Cuenta, Compra, Cliente, Venta
# Create your views here.


def index(request):
    cuenta = Cuenta.objects.all()
    proveedor = Proveedor.objects.all()
    compra = Compra.objects.all()
    cliente = Cliente.objects.all()
    venta = Venta.objects.all()
    return render(request, 'index.html', {'cuentas': cuenta, 'proveedor': proveedor, 'compra': compra, 'cliente': cliente, 'venta': venta})

def cuenta(request, id):
    cuenta = Cuenta.objects.get(id=id)
    venta = Venta.objects.filter(cuenta=cuenta)
    return render(request, 'porcuenta.html', {'cuenta': cuenta, 'venta': venta})