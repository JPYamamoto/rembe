from core.calendarAPI.calendarAPI import fetch_token, make_event
from django.views.generic import View
from core.models.tarjeta import Tarjeta

class CalendarOauth(View):
    """
    Vista auxiliar para redirigir la autorización para Calendar
    """
    
    def get(self, request, *args, **kwargs):
        redirect_fetch_token = fetch_token(request) # Hacemos que se guarde las credenciales y obtenemos el redirect URL
        
        tarjeta = Tarjeta.objects.filter(autor=request.user).first() # Buscamos la tarjeta que se acaba de guardar
        
        make_event(tarjeta.fecha_vencimiento, tarjeta.nombre, request) # Creamos el evento
        
        return redirect_fetch_token
    
