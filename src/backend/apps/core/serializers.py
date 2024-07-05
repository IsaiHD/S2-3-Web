from rest_framework import serializers
from .models import SucursalGtd, ProductoGtd, PlanesGtd, KnowledgeBase, LogsChat

class SucursalGtdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucursalGtd
        fields = ['id', 'nombre_sucursal', 'ubicacion']

class ProductoGtdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoGtd
        fields = ['id', 'product_name', 'description']

class PlanesGtdSerializer(serializers.ModelSerializer):
    id_producto = ProductoGtdSerializer()  # Nested serializer for product details
    class Meta:
        model = PlanesGtd
        fields = ['id', 'id_producto', 'price', 'id_knowledge']

class KnowledgeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBase
        fields = ['id', 'tema', 'subtema', 'pregunta', 'respuesta']

class LogsChatSerializer(serializers.ModelSerializer):
    id_sucursal = SucursalGtdSerializer()      # Nested serializers for related data
    id_producto = ProductoGtdSerializer()
    class Meta:
        model = LogsChat
        fields = ['chat_id', 'chat_type', 'chat_description', 'chat_date',
                  'chat_pregunta', 'chat_respuesta', 'id_sucursal', 'id_producto']
