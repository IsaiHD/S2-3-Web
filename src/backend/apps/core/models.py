from django.db import models

class SucursalGtd(models.Model):
    nombre_sucursal = models.CharField(max_length=100)  # Adjust length as needed
    ubicacion = models.CharField(max_length=200)       # Adjust length as needed

class ProductoGtd(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()

class PlanesGtd(models.Model):
    id_producto = models.ForeignKey(ProductoGtd, on_delete=models.CASCADE)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    id_knowledge = models.ForeignKey('KnowledgeBase', on_delete=models.CASCADE)

class KnowledgeBase(models.Model):
    tema = models.CharField(max_length=100)
    subtema = models.CharField(max_length=100, blank=True, null=True)
    pregunta = models.TextField()
    respuesta = models.TextField()

class LogsChat(models.Model):
    chat_id = models.AutoField(primary_key=True)  # Assuming an auto-incrementing ID
    chat_type = models.CharField(max_length=50)  # E.g., 'Consulta', 'Soporte', etc.
    chat_description = models.TextField()
    chat_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    chat_pregunta = models.TextField()
    chat_respuesta = models.TextField()

    id_sucursal = models.ForeignKey(SucursalGtd, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(ProductoGtd, on_delete=models.CASCADE)
