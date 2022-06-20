from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from simple_history.models import HistoricalRecords

from io import StringIO, BytesIO

# Model for User entities
# It's the default provided by Django.
User=get_user_model()

class Tarjeta(models.Model):
    """Model for notes with default behaviour provided by the base Django model.
    Fields:
        - nombre
        - autor
        - colaboradores
        - fecha_vencimiento
        - fecha_modificacion
        - contenido
        - contenido_reverso
        - tema
        - history
    """

    nombre = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    colaboradores = models.ManyToManyField(User, related_name="collaborators")
    fecha_vencimiento = models.DateTimeField(null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # Markdown fields: automatically handled by `markdownx` both in models and templates.
    contenido = MarkdownxField(blank=False)
    contenido_reverso = MarkdownxField(blank=True)

    class Tema(models.IntegerChoices):
        """Enumeration class for the themes provided by the system."""
        DEFAULT  = 0, _('Default')
        SPLENDOR = 1, _('Splendor')
        RETRO    = 2, _('Retro')
        AIR      = 3, _('Air')
        MODEST   = 4, _('Modest')

    tema = models.IntegerField(choices=Tema.choices, blank=False, null=False, default=Tema.DEFAULT)

    # History for version control.
    history = HistoricalRecords()

    def __str__(self):
        """String representation of the model.
        Provided to be used by the Django admin.
        """

        return "{} ({})".format(self.nombre, self.fecha_modificacion)

    def to_markdown_file(self):
        """Generates an in-memory file object with the content of the note
        in markdown format.

        At the top of the file comes a front matter with meta-data, followed
        by the front content of the note and finally the reverse content.

        The return type is an instance of io.BytesIO
        """
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
