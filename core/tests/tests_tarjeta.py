from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from django.test import TestCase

from datetime import datetime

from core.models.tarjeta import Tarjeta

CONTENIDO="""# Hola Mundo

Este es un ejemplo de contenido escrito en **Markdown** para una tarjeta.

La siguiente es una _lista_:
- Elemento 1
- Elemento 2
"""

CONTENIDO_REVERSO="""# Contenido extra

El siguiente es un video de YouTube:

{{ https://www.youtube.com/watch?v=iik25wqIuFo }}
"""

class TarjetaTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rembetest', email='test@rembe.azurewebsites.net', password='rembepassword')

        tarjeta = Tarjeta.objects.create(
            nombre='Ejemplo Tarjeta',
            autor=self.user,
            fecha_vencimiento=make_aware(datetime.now()),
            contenido=CONTENIDO,
            contenido_reverso=CONTENIDO_REVERSO,
            tema=Tarjeta.Tema.DEFAULT,
        )

        self.tarjeta_id = tarjeta.pk

    def clona_tarjeta(self):
        tarjeta = Tarjeta.objects.get(pk=self.tarjeta_id)
        tarjeta.pk = None
        tarjeta.save()

        return tarjeta


    def test_tarjeta_creada_correctamente(self):
        tarjeta = Tarjeta.objects.get(pk=self.tarjeta_id)

        self.assertIsNotNone(tarjeta)

        self.assertEqual(tarjeta.nombre, "Ejemplo Tarjeta")
        self.assertEqual(tarjeta.autor, self.user)
        self.assertTrue(tarjeta.fecha_vencimiento <= tarjeta.fecha_modificacion)
        self.assertEqual(tarjeta.contenido, CONTENIDO)
        self.assertEqual(tarjeta.contenido_reverso, CONTENIDO_REVERSO)
        self.assertEqual(tarjeta.tema, Tarjeta.Tema.DEFAULT)

    def test_modificacion(self):
        # Nueva tarjeta
        tarjeta = self.clona_tarjeta()

        self.assertTrue(len(tarjeta.history.all()) == 1)

        # Verifica modificación
        tarjeta.nombre = "Tarjeta 2"
        tarjeta.save()

        tarjeta_verif = Tarjeta.objects.get(pk=tarjeta.pk)

        self.assertIsNotNone(tarjeta_verif)
        self.assertEqual(tarjeta_verif.pk, tarjeta.pk)
        self.assertNotEqual(self.tarjeta_id, tarjeta.pk)

        self.assertEqual(tarjeta_verif.nombre, "Tarjeta 2")
        self.assertEqual(tarjeta_verif.autor, tarjeta.autor)
        self.assertEqual(tarjeta_verif.fecha_vencimiento, tarjeta.fecha_vencimiento)
        self.assertEqual(tarjeta_verif.contenido, tarjeta.contenido)
        self.assertEqual(tarjeta_verif.contenido_reverso, tarjeta.contenido_reverso)
        self.assertEqual(tarjeta_verif.tema, tarjeta.tema)

        self.assertTrue(len(tarjeta.history.all()) == 2)

    def test_versiones(self):
        # Nueva tarjeta
        tarjeta = self.clona_tarjeta()

        self.assertTrue(len(tarjeta.history.all()) == 1)

        # Verifica modificación
        tarjeta.nombre = "Tarjeta 2"
        tarjeta.save()

        self.assertTrue(len(tarjeta.history.all()) == 2)

        primera_tarjeta = tarjeta.history.earliest()
        self.assertIsNotNone(primera_tarjeta)

        self.assertNotEqual(primera_tarjeta.nombre, tarjeta.nombre)
        self.assertEqual(primera_tarjeta.nombre, "Ejemplo Tarjeta")
        self.assertEqual(primera_tarjeta.autor, tarjeta.autor)
        self.assertEqual(primera_tarjeta.fecha_vencimiento, tarjeta.fecha_vencimiento)
        self.assertEqual(primera_tarjeta.contenido, tarjeta.contenido)
        self.assertEqual(primera_tarjeta.contenido_reverso, tarjeta.contenido_reverso)
        self.assertEqual(primera_tarjeta.tema, tarjeta.tema)

    def test_to_markdown(self):
        tarjeta = Tarjeta.objects.get(pk=self.tarjeta_id)
        file_stream = tarjeta.to_markdown_file()

        contenido = file_stream.getvalue()
        contenido = contenido.decode("utf-8")
        self.assertIn("nombre: {}".format(tarjeta.nombre), contenido)
        self.assertIn("autor: {}".format(tarjeta.autor.username), contenido)
        self.assertIn("fecha_vencimiento: {}".format(tarjeta.fecha_vencimiento), contenido)
        self.assertIn(tarjeta.contenido, contenido)
        self.assertIn(tarjeta.contenido_reverso, contenido)
