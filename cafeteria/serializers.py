from rest_framework import serializers
from .models import *

class CafeteriaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cafeteria
        fields= "__all__"
    
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields= "__all__"

class RolesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Roles
        fields= "__all__" 

class UsuariosSerializers(serializers.ModelSerializer):
    rol = RolesSerializers(source='id_rol', read_only=True)
    class Meta:
        model= Usuarios
        fields= "__all__" 

class PedidoSerializers(serializers.ModelSerializer):
    usuarios = UsuariosSerializers(source='id_usuario', read_only=True)
    class Meta:
        model= Pedido
        fields= "__all__"

class ProductoSerializers(serializers.ModelSerializer):
    categoria = CategoriaSerializers(source='id_categoria', read_only=True)
    class Meta:
        model= Producto
        fields= "__all__"
        
class DetallePedidoSerializers(serializers.ModelSerializer):
    pedido = PedidoSerializers(source='id_pedido', read_only=True)
    producto = ProductoSerializers(source='id_producto', read_only=True)
    class Meta:
        model= DetallePedido
        fields= "__all__"

class PagoSerializers(serializers.ModelSerializer):
    pedido = PedidoSerializers(source='id_pedido', read_only=True)
    class Meta:
        model= Pago
        fields= "__all__"
  