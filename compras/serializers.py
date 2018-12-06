from .models import Usuario, Lista, Producto, ProductoCliente, Tienda
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'name', 'age', 'password')
 
class ListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lista
        fields = ('id_pk', 'email', 'name', 'total_productos', 'total_productos_comprados', 'total_presupuestado', 'total_real')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id_pk', 'name', 'description', 'price', 'email', 'image')

class ProductoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductoCliente
        fields = ('id_producto_cliente', 'id_lista', 'id_producto')

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('id_pk','email','name','nombre_sucursal','direccion','ciudad','region')