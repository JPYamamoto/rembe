from google.auth.transport.requests import Request
import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import googleapiclient.discovery

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from datetime import timedelta

from core.models.token import Token
from core.models import Token

CLIENT_ID = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id']
CLIENT_SECRET = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['secret']
SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.events']
TOKEN_URI = 'https://oauth2.googleapis.com/token'
TIME_ZONE = "America/Mexico_City"

CLIENT_CONFIG = {'web': {
    'client_id': CLIENT_ID,
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': TOKEN_URI,
    "redirect_uris": ["https://localhost","http://localhost", "urn:ietf:wg:oauth:2.0:oob", 'https://127.0.0.1:8000/tarjetas/', 'https://rembe.azurewebsites.net/tarjetas/', 'https://rembe.azurewebsites.net/tarjetas/create/', 'https://rembe.azurewebsites.net/tarjetas/redirect/'],
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_secret': CLIENT_SECRET
    }}

def get_credentials(request):
    """
    Método que genera las credenciales para acceder a Google Calendar API,
    primero busca las credeciales en la Base de Datos, y si no están las genera y 
    las guardas

    Args:
        user (User): Usuario a buscar

    Returns:
        Credentials: Credenciales del usuario
    """

    token = Token.objects.get(user=request.user)
            
    creds = Credentials(
        token = token.token,
        refresh_token = token.refresh_token,
        token_uri= TOKEN_URI,
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        scopes=SCOPES
    )
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())

    return creds

def get_authorization_url():
    """
    Método que regresa el authorization_url

    Returns:
        str: authorization_url
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        redirect_uri='https://rembe.azurewebsites.net/tarjetas/redirect/')
    
    authorization_url, _ = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'
    )
    
    return authorization_url

def fetch_token(request):
    """
    Método que obtiene las credenciales, las guarda
    y regresa a la página principasl

    Args:
        request (request): request hacia Oauth

    Returns:
        redirect: redirección a la página princiapl
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=None,
        redirect_uri='https://rembe.azurewebsites.net/tarjetas/redirect/')
    
    flow.fetch_token(code=request.GET.get('code'))
    
    creds = flow.credentials
    token = Token(token=creds.token, refresh_token=creds.refresh_token, user=request.user)
    token.save()
    return redirect('https://rembe.azurewebsites.net/tarjetas/create/')
    
    

def create_credentials():
    """
    Método que genera las credenciales de un usuario por primera vez

    Args:
        user (User): Usuario

    Returns:
        redirect: redirección a el authorization_url
    """

    
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        redirect_uri='https://rembe.azurewebsites.net/tarjetas/redirect/')
    
   
    auth_url = get_authorization_url()
    
    return redirect(auth_url)

    


def make_event(fecha, nombre, request):
    """
    Método para generar un evento e insertarlo en el calendario del usuario

    Args:
        fecha (datetime): Fecha del evento
        nombre (str): Nombre del evento
        user (User): Usuario actual
    """
    

    credentials = get_credentials(request)
    
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    
    
    fecha_final = fecha + timedelta(hours=24)

    event = {
            'summary': nombre,
            'location': 'Mexico',
            'start': {
                'dateTime': fecha.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': TIME_ZONE,
            },
            'end': {
                'dateTime': fecha_final.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': TIME_ZONE,
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    service.events().insert(calendarId='primary', body=event).execute()
