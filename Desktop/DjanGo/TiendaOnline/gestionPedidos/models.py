from django.db import models

# video 24 quedo algo pendiente de envio de formulario
# Create your models here.  Quedamos en el video 27

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La direccion")
    emial=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=11)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)
    


class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()



