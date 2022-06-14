from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from simple_history.models import HistoricalRecords

from io import StringIO, BytesIO

# Create your models here.

User=get_user_model()

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    colaboradores = models.ManyToManyField(User, related_name="collaborators")
    fecha_vencimiento = models.DateTimeField(null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    contenido = MarkdownxField(blank=False)
    contenido_reverso = MarkdownxField(blank=True)

    class Tema(models.IntegerChoices):
        DEFAULT  = 0, _('Default')
        SPLENDOR = 1, _('Splendor')
        RETRO    = 2, _('Retro')
        AIR      = 3, _('Air')
        MODEST   = 4, _('Modest')

    tema = models.IntegerField(choices=Tema.choices, blank=False, null=False, default=Tema.DEFAULT)
    history = HistoricalRecords()

    def __str__(self):
        return "{} ({})".format(self.nombre, self.fecha_modificacion)

    def to_markdown_file(self):
        content = (
            "---\n"
            + "nombre: {}\n".format(self.nombre)
            + "autor: {}\n".format(self.autor.username)
            + "fecha_vencimiento: {}\n".format(self.fecha_vencimiento)
            + "fecha_modificacion: {}\n".format(self.fecha_modificacion)
            + "---\n"
            + self.contenido
            + "\n---\n"
            + self.contenido_reverso
        )

        bytes_content = content.encode('utf-8')

        file_content = BytesIO()
        file_content.write(bytes_content)

        return file_content
