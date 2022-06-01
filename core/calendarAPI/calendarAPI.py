from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from allauth.socialaccount.models import SocialToken, SocialApp
import googleapiclient.discovery
from datetime import timedelta
from core.models.token import Token

from core.models import Token
import environ

env = environ.Env()

CLIENT_ID = env("GOOGLE_CLIENT_ID")
CLIENT_SECRET = env("GOOGLE_SECRET")
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']
TOKEN_URI = 'https://oauth2.googleapis.com/token'

TIME_ZONE = "America/Mexico_City"

def get_credentials(user):
    """
    Método que genera las credenciales para acceder a Google Calendar API,
    primero busca las credeciales en la Base de Datos, y si no están las genera y 
    las guardas

    Args:
        user (User): Usuario a buscar

    Returns:
        Credentials: Credenciales del usuario
    """
    token_exists = Token.objects.filter(user=user)

    
    if not token_exists.exists():
        return create_credentials(user)
    
    token = Token.objects.get(user=user)
            
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

def create_credentials(user):
    """
    Método que genera las credenciales de un usuario por primera vez

    Args:
        user (User): Usuario

    Returns:
        Credentials: Credenciales del usuario
    """
    
    CLIENT_CONFIG = {'web': {
    'client_id': CLIENT_ID,
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': TOKEN_URI,
    "redirect_uris": ["https://localhost","http://localhost", "urn:ietf:wg:oauth:2.0:oob", 'https://127.0.0.1:8000/tarjetas/', 'https://rembe.azurewebsites.net/tarjetas/'],
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_secret': CLIENT_SECRET
    }}
    
    flow = InstalledAppFlow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        redirect_uri='https://127.0.0.1:8000/tarjetas/')
    
    creds = flow.run_local_server()
    print(f"REFRESH_TOKEN: {creds.refresh_token}")
    
    # Guardamos los tokens en la BDD
    token = Token(token=creds.token, refresh_token=creds.refresh_token, user=user)
    token.save() 
    
    return creds

    


def make_event(fecha, nombre, user):
    """
    Método para generar un evento e insertarlo en el calendario del usuario

    Args:
        fecha (datetime): Fecha del evento
        nombre (str): Nombre del evento
        user (User): Usuario actual
    """
    

    credentials = get_credentials(user)
    
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    
    result = service.calendarList().list().execute()
    calendar_id = result['items'][0]['id'] # Calendario principal
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
    service.events().insert(calendarId=calendar_id, body=event).execute()

 