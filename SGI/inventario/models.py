from django.db import models

# Create your models here.

class producto(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10000)
    nombre=models.CharField(max_length=100)
    cantidad=models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre, self.cantidad)
    
class proveedor(models.Model):
    cedula=models.CharField(primary_key=True,max_length=1000000000)
    nombreproveedor=models.CharField(max_length=100)
    direccion=models.CharField(max_length=1000000)
    telefono=models.CharField(max_length=1000000000)
    email=models.EmailField()

    def __str__(self):
        texto1="{0} ({1})"
        return texto1.format(self.nombreproveedor, self.direccion,self.telefono,self.email)

class factura(models.Model):
    numerofactura=models.CharField(primary_key=True,max_length=10000)
    cliente=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    valor=models.PositiveBigIntegerField()

    def __str__(self):
        texto3="{0} ({1})"
        return texto3.format(self.cliente,self.estado,self.valor)

class proveedora(models.Model):
     id=models.CharField(primary_key=True,max_length=1000000000)
     nombreproveedora=models.CharField(max_length=100)
     direcciones=models.CharField(max_length=1000000)
     contacto=models.CharField(max_length=1000000000)
     correo=models.EmailField()

     def __str__(self):
        texto2="{0} ({1})"
        return texto2.format(self.id, self.nombreproveedora,self.direcciones,self.correo)
