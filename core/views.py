from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, resolve
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from core.models import Tarjeta
from core.forms import TarjetaForm

# Create your views here.


class CrearTarjeta(LoginRequiredMixin, CreateView):
    queryset = Tarjeta.objects.all()
    login_url = '/accounts/login'
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/form.html'
    success_url = reverse_lazy('tarjetas:index')

class CrearTarjeta(LoginRequiredMixin, CreateView):
    queryset = Tarjeta.objects.all()
    login_url = reverse_lazy('auth:login')
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/form.html'
    success_url = reverse_lazy('tarjetas:index')
