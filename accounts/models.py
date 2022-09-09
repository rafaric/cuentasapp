from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    servicio = models.CharField(max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    cant_perfiles = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.correo
    

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    def __str__(self):
        string = str(self.fecha) +" | " + str(self.cuenta)
        return (string)
    
class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    perfiles = models.IntegerField(default=0)
    
    def __str__(self):
        string = str(self.fecha) +" | " + str(self.cuenta)+" | "+str(self.perfiles)
        return (string)