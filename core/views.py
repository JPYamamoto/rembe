from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from core.models import Tarjeta, CuerpoTarjeta

# Create your views here.


class TarjetaView(ListView):
    queryset = Tarjeta.objects.all()
    
class CuerpoTarjetaView(ListView):
    queryset = CuerpoTarjeta.objects.all()
