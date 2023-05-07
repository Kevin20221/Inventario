from django.urls import path
from . import views

urlpatterns=[
    path('proveedor/',views.proveedor, name="proveedor"),
    path('proveedora/',views.proveedoras, name="proveedoras"),
    path('factura/',views.facturas, name="factura"),
    path('', views.home),
    path('registrarfactura/', views.registrarfactura),
    path('registrarproducto/', views.registrarproducto),
    path('edicionproducto/<codigo>', views.edicionproducto),
    path('editarproducto/', views.editarproducto),
    path('eliminarproducto/<codigo>', views.eliminarproducto),
    path('factura/eliminarfactura/<numerofactura>', views.eliminarfactura),
    path('factura/edicionfactura/<numerofactura>', views.edicionfactura),
    path('editarfactura/', views.editarfactura),
    path('factura/agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('proveedora/eliminarproveedora/<id>', views.eliminarproveedora),
    path('registrarproveedor/', views.registrarproveedor),
    path('proveedora/edicionproveedora/<id>', views.edicionproveedora),
    path('editarproveedor/', views.editarproveedor),
    path('proveedora/',views.proveedoras),
    path('proveedora/factura/',views.facturas),
    path('factura/proveedora/',views.proveedoras),
    path('descargar-facturas/', views.descargar_facturas, name='descargar_facturas'),
    path('login/',views.login),
    path('proveedora/factura/proveedora/',views.proveedoras),
    path('proveedora/factura/proveedora/factura/',views.facturas),
    path('factura/proveedora/factura/',views.facturas),
    path('factura/factura/',views.facturas),

]