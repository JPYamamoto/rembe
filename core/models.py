from django.db import models

# Create your models here.


class Tarjeta(models.Model):
    NombreTarjeta = models.CharField(max_length=50)
    FechaVencimiento = models.DateTimeField(null=True)

    def __str__(self):
        return self.NombreTarjeta


class cuerpoTarjeta(models.Model):
    Tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    FechaModificacion = models.DateTimeField(auto_now=True)
    Contenido = models.TextField(blank=True)
    ContenidoReverso = models.TextField(blank=True)

    def __str__(self):
        return "Ultima modificacion: \n" + str(self.FechaModificacion) + "\n***Frente\n" + self.Contenido + "\n***ParteTrasera\n" + self.ContenidoReverso
