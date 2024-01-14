from django.db import models

    
class Proveedor(models.Model):
    _id =models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    nacionalidad= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    


class Categoria(models.Model):
    _id=models.PositiveIntegerField()
    nombre= models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    _id=models.PositiveIntegerField()
    nombre= models.CharField(max_length=100)
    imagen= models.CharField(max_length=100, null=True)
    precio=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    proveedor= models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.nombre