from django.shortcuts import render, redirect
from .models import producto
from django.contrib import messages
from .models import proveedor
from .models import factura
from .models import proveedora
from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    busqueda=request.GET.get("buscar")
    productos= producto.objects.all()
    if busqueda:
        productos=producto.objects.filter(
              Q(nombre__icontains=busqueda) |
              Q(codigo__icontains=busqueda)
            
        ).distinct()
    return render(request, "gestionproductos.html",{"productos":productos})

def registrarproducto(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    cantidad = request.POST['numcantidad']

    productos=producto.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    messages.success(request,'Producto registrado')



    return redirect ('/')




def edicionproducto(request, codigo):
    productos=producto.objects.get(codigo=codigo)

    return render (request, "edicionproducto.html",{"productos":productos})



def eliminarproducto(request,codigo):
    productos=producto.objects.get(codigo=codigo)
    productos.delete()

    messages.success(request,'Producto eliminado')

    return redirect ('/')

def editarproducto(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    cantidad = request.POST['numcantidad']
    productos=producto.objects.get(codigo=codigo)
    productos.nombre=nombre
    productos.cantidad=cantidad
    productos.save()
    
    messages.success(request,'!Producto editado!')

    return redirect ('/')







def proveedores(request):
    proveedores = proveedor.objects.all()
    return render(request, "proveedores.html",{"proveedor":proveedores})

def facturas(request):
    facturas=factura.objects.all()

    busqueda=request.GET.get("buscar")
    facturas= factura.objects.all()
    if busqueda:
        facturas=factura.objects.filter(
              Q(numerofactura__icontains=busqueda) |
              Q(cliente__icontains=busqueda) |
              Q(estado__icontains=busqueda)
              

            
        ).distinct()


    return render(request,"gestionfacturas.html",{"facturas":facturas})

def registrarfactura(request):
    numerofactura = request.POST['txtfactura']
    cliente = request.POST['txtcliente']
    estado= request.POST['txtestado']
    valor = request.POST['valor']

    facturas=factura.objects.create(numerofactura=numerofactura, cliente=cliente, estado=estado, valor=valor)
    messages.success(request,'¡Factura registrada!')
    return redirect('/')



def eliminarfactura(request,numerofactura):
    facturas=factura.objects.get(numerofactura=numerofactura)
    facturas.delete()
    messages.success(request,'¡Factura eliminada!')
    return redirect('/')

def edicionfactura(request, numerofactura):
    facturas=factura.objects.get(numerofactura=numerofactura)
    return render(request, 'edicionfactura.html',{"facturas":facturas})

def editarfactura(request):
    numerofactura = request.POST['txtfactura']
    cliente = request.POST['txtcliente']
    estado= request.POST['txtestado']
    valor = request.POST['valor']

    facturas=factura.objects.get(numerofactura=numerofactura)
    facturas.numerofactura=numerofactura
    facturas.cliente=cliente
    facturas.estado=estado
    facturas.valor=valor
    facturas.save()
    messages.success(request,'¡Factura editada!')

    return redirect('/')

def descargar_facturas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM inventario_factura")
        datos = cursor.fetchall()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="facturas.csv"'

    escritor_csv = csv.writer(response)
    encabezado = [campo[0] for campo in cursor.description]
    escritor_csv.writerow(encabezado)
    escritor_csv.writerows(datos)

    return response

def agregarproducto(request, producto=None, numerofactura=None):
    Factura = get_object_or_404(factura, numerofactura=numerofactura)

    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre_producto')
        precio_producto = request.POST.get('precio_producto')
        cantidad_producto = request.POST.get('cantidad_producto')

        producto = producto.objects.create(
            nombre=nombre_producto,
            precio=precio_producto,
            cantidad=cantidad_producto,
            factura=Factura
        )

        # Actualizar el valor total de la factura
        Factura.valor += (producto.precio * producto.cantidad)
        Factura.save()

        return redirect('detallefactura', numerofactura=numerofactura)

    return render(request, 'gestionproductos.html', {'factura': factura})
    return render(request, '/')

def proveedoras(request):
    proveedoras=proveedora.objects.all()

    busqueda=request.GET.get("buscar")
    proveedoras= proveedora.objects.all()
    if busqueda:
        proveedoras=proveedora.objects.filter(
              Q(id__icontains=busqueda) |
              Q(nombreproveedora__icontains=busqueda)
             
            
              

            
        ).distinct()


    return render(request, "gestionproveedor.html",{"proveedoras":proveedoras})


def eliminarproveedora(request,id):
    proveedoras=proveedora.objects.get(id=id)
    proveedoras.delete()
    messages.success(request,'¡Proveedor eliminado!')
    return redirect('/')

def registrarproveedor(request):
    id = request.POST['id']
    nombreproveedora= request.POST['txtnombre']
    direcciones= request.POST['txtdireccion']
    contacto= request.POST['txttel']
    correo = request.POST['txtcorreo']
    

    proveedoras=proveedora.objects.create(id=id,nombreproveedora=nombreproveedora,direcciones=direcciones,contacto=contacto,correo=correo)
    messages.success(request,'¡Proveedor registrado!')
    return redirect('/')

def edicionproveedora(request, id):
    proveedoras=proveedora.objects.get(id=id)
    return render(request, 'edicionproveedor.html',{"proveedoras":proveedoras})
    

def editarproveedor(request):
     id = request.POST['id']
     nombreproveedora= request.POST['txtnombre']
     direcciones= request.POST['txtdireccion']
     contacto= request.POST['txttel']
     correo = request.POST['txtcorreo']

     proveedoras=proveedora.objects.get(id=id)
     proveedoras.id=id
     proveedoras.nombreproveedora=nombreproveedora
     proveedoras.direcciones=direcciones
     proveedoras.contacto=contacto
     proveedoras.correo=correo
     proveedoras.save()
     messages.success(request,'¡Proveedor editado!')

     return redirect('/')

def login(request):
   if request.method=='GET':
    return render(request, "login.html",{'form':UserCreationForm})
   
   else:
       if request.POST['password1'] == request.POST['password2']:
           try:
                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                 user.save()
                 return redirect('/')
           except:
            return render(request, 'login.html',{'form':UserCreationForm,"error":'El usuario ya esta registrado'})
           
       return render(request, 'login.html',{'form':UserCreationForm,"error":'Las contraseñas no coiciden'})



