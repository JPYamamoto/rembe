from core.calendarAPI.calendarAPI import fetch_token
from django.views.generic import View

class CalendarOauth(View):
    """View that on any HTTP GET request will try to
    fetch the token of the currently logged-in user.
    """
    def get(self, request, *args, **kwargs):
        return fetch_token(request)
