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

CONTENIDO2 = "HEY"

CONTENIDO_REVERSO="""# Contenido extra

El siguiente es un video de YouTube:

{{ https://www.youtube.com/watch?v=iik25wqIuFo }}
"""

CONTENIDO_REVERSO2="""# Contenido extra

TEST VIDEO2:

{{ https://www.youtube.com/watch?v=aljfbhxtdyc }}
"""


class ListarTarjetaTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rembetestListView', email='test@rembe.azurewebsites.net', password='rembepassword')

    def test_no_tarjetas(self):
        self.assertFalse(Tarjeta.objects.filter(autor=self.user).exists())
        
    def test_get_all_tarjetas(self):
        tarjeta1 = Tarjeta.objects.create(
            nombre='Ejemplo1 Tarjeta',
            autor=self.user,
            fecha_vencimiento=make_aware(datetime.now()),
            contenido=CONTENIDO,
            contenido_reverso=CONTENIDO_REVERSO,
            tema=Tarjeta.Tema.DEFAULT,
        )
        
        tarjeta1.save()
        self.assertQuerysetEqual(Tarjeta.objects.filter(autor=self.user), [tarjeta1])
        
        tarjeta2 = Tarjeta.objects.create(
            nombre='Ejemplo2 Tarjeta',
            autor=self.user,
            fecha_vencimiento=make_aware(datetime.now()),
            contenido=CONTENIDO,
            contenido_reverso=CONTENIDO_REVERSO2,
            tema=Tarjeta.Tema.DEFAULT,
        )
        
        tarjeta2.save()
        self.assertQuerysetEqual(Tarjeta.objects.filter(autor=self.user), [tarjeta1, tarjeta2], ordered=False)
        
        
class VerTarjetaTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rembetestListView', email='test@rembe.azurewebsites.net', password='rembepassword')

    def test_codigo_ver_tarjeta(self):
        tarjeta = Tarjeta.objects.create(
            nombre='Ejemplo Tarjeta',
            autor=self.user,
            fecha_vencimiento=make_aware(datetime.now()),
            contenido=CONTENIDO,
            contenido_reverso=CONTENIDO_REVERSO,
            tema=Tarjeta.Tema.DEFAULT,
        )
        
        tarjeta.save()
        pk = tarjeta.pk
        
        url = "tarjetas/view/" + str(pk) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        
class EditarTarjetaTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='rembetestListView', email='test@rembe.azurewebsites.net', password='rembepassword')

    def test_editar_contenido(self):
        tarjeta = Tarjeta.objects.create(
            nombre='Ejemplo Tarjeta',
            autor=self.user,
            fecha_vencimiento=make_aware(datetime.now()),
            contenido=CONTENIDO,
            contenido_reverso=CONTENIDO_REVERSO,
            tema=Tarjeta.Tema.DEFAULT,
        )
        
        tarjeta.save()
        pk = tarjeta.pk
        
        tarjeta_obtenida = Tarjeta.objects.get(pk=pk)
        tarjeta_obtenida.contenido = CONTENIDO2
        tarjeta_obtenida.save()
        pk = tarjeta_obtenida.pk
        
        tarjeta_obtenida2 = Tarjeta.objects.get(pk=pk)
        self.assertEqual(tarjeta_obtenida2.contenido, CONTENIDO2)
        
        
        

        
    
        