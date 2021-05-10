from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=25)
    annos = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Mascota(models.Model):
    nombre = models.CharField(primary_key=True,max_length=25)
    edad = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mascotas',null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
        