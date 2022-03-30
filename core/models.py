from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    nombre_tarjeta = models.CharField(max_length=50)
    fecha_vencimiento = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre_tarjeta


class CuerpoTarjeta(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    contenido = models.TextField(blank=True)
    contenido_reverso = models.TextField(blank=True)

    def __str__(self):
        return "Ultima modificacion: \n" + str(self.fecha_modificacion) + "\n***Frente\n" + self.contenido + "\n***ParteTrasera\n" + self.contenido_reverso