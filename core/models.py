from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Tarjeta(models.Model):
    nombre_tarjeta = models.CharField(max_length=50)
    fecha_vencimiento = models.DateTimeField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    collaborators = models.ManyToManyField(User, related_name="collaborators")

    def __str__(self):
        return self.nombre_tarjeta


class CuerpoTarjeta(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    contenido = models.TextField(blank=True)
    contenido_reverso = models.TextField(blank=True)

    def __str__(self):
        return "Ultima modificacion: \n" + str(self.fecha_modificacion) + "\n***Frente\n" + self.contenido + "\n***ParteTrasera\n" + self.contenido_reverso
