from django.db import models
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField
import reversion

# Create your models here.

User=get_user_model()

@reversion.register()
class Tarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    colaboradores = models.ManyToManyField(User, related_name="collaborators")
    fecha_vencimiento = models.DateTimeField(null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    contenido = MarkdownxField(blank=False)
    contenido_reverso = MarkdownxField(blank=True)

    def __str__(self):
        return "{} ({})".format(self.nombre, self.fecha_modificacion)
