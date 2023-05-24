from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 
    
class Pedidos(models.Model):
    fecha = models.DateField 
    usuario = models.ForeignKey("User", verbose_name=("email"), on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=100) 
    cantidad_mesa = models.IntegerField(100)
    cantidad_sillones = models.IntegerField(100)
    cantidad_puff = models.IntegerField(100)
    comentarios = models.TextField()
    nombre_producto = models.ForeignKey("Producto", verbose_name=("id_producto"), on_delete=models.CASCADE)      
    total_pedido = models.IntegerField(100) 
    estado = models.CharField(max_length=100)
    
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)   
    descripcion_producto = models.TextField()
    precio_producto = models.IntegerField(100)
    
    