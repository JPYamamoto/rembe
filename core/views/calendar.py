from core.calendarAPI.calendarAPI import fetch_token
from django.views.generic import View

class  CalendarOauth(View):
    def get(self, request, *args, **kwargs):
        return fetch_token(request)