from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from core.models.tarjeta import Tarjeta
from core.models.token import Token
from core.forms import TarjetaForm

from core.calendarAPI.calendarAPI import make_event, create_credentials

class ListarTarjeta(LoginRequiredMixin, ListView):
    model = Tarjeta
    template_name = 'tarjeta/list.html'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)


class VerTarjeta(LoginRequiredMixin, DetailView):
    model = Tarjeta
    template_name = 'tarjeta/view.html'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)

    def get_object(self):
        obj = super().get_object()
        version = self.request.GET.get('version', None)

        if version:
            obj = obj.history.all().filter(pk=int(version)).get()

        return obj


class HistorialTarjeta(LoginRequiredMixin, ListView):
    model = Tarjeta
    template_name = 'tarjeta/history.html'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user).get().history.all()


class CrearTarjeta(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/form.html'
    success_url = reverse_lazy('tarjetas:index')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.fecha_modificacion = timezone.now()
        
        # Hacemos lo de calendar
        
        if not Token.objects.filter(user=self.request.user).exists():
            return create_credentials()
        
        make_event(form.instance.fecha_vencimiento, form.instance.nombre, request=self.request)
        return super(CrearTarjeta, self).form_valid(form)


class EditarTarjeta(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/form.html'

    def form_valid(self, form):
        form.instance.fecha_modificacion = timezone.now()
        return super(EditarTarjeta, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('tarjetas:view', args=(self.object.id, ))


class EliminarTarjeta(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Tarjeta
    template_name = 'tarjeta/delete_form.html'
    success_url = reverse_lazy('tarjetas:index')
