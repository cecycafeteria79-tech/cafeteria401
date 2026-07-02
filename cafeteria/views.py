from rest_framework import viewsets
from .models import *
from .serializers import * 

class CafeteriaViewSet(viewsets.ModelViewSet):
    queryset= Cafeteria.objects.all()
    serializer_class= CategoriaSerializers

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset= Categoria.objects.all()
    serializer_class=CategoriaSerializers
class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.select_related('id_categoria').all()
    serializer_class= ProductoSerializers

class RolesViewSet(viewsets.ModelViewSet):
    queryset= Roles.objects.all()
    serializer_class= RolesSerializers 

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset= Usuarios.objects.select_related('id_rol').all()
    serializer_class= UsuariosSerializers

class PedidoViewSet(viewsets.ModelViewSet):
    queryset= Pedido.objects.select_related('id_usuario').all()
    serializer_class=PedidoSerializers
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset= DetallePedido.objects.select_related('id_pedido', 'id_producto').all()
    serializer_class= DetallePedidoSerializers

class PagoViewSet(viewsets.ModelViewSet):
    queryset= Pago.objects.select_related('id_pedido').all()
    serializer_class= PagoSerializers
