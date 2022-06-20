from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404, FileResponse

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from core.models.tarjeta import Tarjeta
from core.models.token import Token
from core.forms import TarjetaForm
from core.calendarAPI.calendarAPI import make_event, create_credentials

class ListarTarjeta(LoginRequiredMixin, ListView):
    """View that renders the list of notes belonging to the logged-in user.

    If the user is not logged-in, they will be redirected to the auth page.
    """

    model = Tarjeta
    template_name = 'tarjeta/list.html'
    login_url = '/accounts/login'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)


class VerTarjeta(LoginRequiredMixin, DetailView):
    """Returns a given note, whose ID was passed as an argument in the URL.

    The user requesting the page has to be the author of the note.
    """

    model = Tarjeta
    template_name = 'tarjeta/view.html'
    login_url = '/accounts/login'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user)

    def get_object(self):
        """When the URL query parameter ?version=<version> is given,
        the appropriate version of the note will be rendered, if it
        exists. Otherwise, the latest version is returned.
        """
        obj = super().get_object()
        version = self.request.GET.get('version', None)

        if version:
            obj = obj.history.all().filter(pk=int(version)).get()

        return obj


class HistorialTarjeta(LoginRequiredMixin, ListView):
    """Returns the list of all versions of the note whose ID was
    passed through the URL.

    The user requesting the page has to be the author of the note.
    """

    model = Tarjeta
    template_name = 'tarjeta/history.html'
    login_url = '/accounts/login'

    def get_queryset(self):
        return self.model.objects.filter(autor=self.request.user).get().history.all()


class CrearTarjeta(LoginRequiredMixin, CreateView):
    """View to create a new note with the currently logged-in user
    as the author.
    """

    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/form.html'
    success_url = reverse_lazy('tarjetas:index')
    login_url = '/accounts/login'

    def form_valid(self, form):
        """Save the note and create a new event in Google Calendar with
        the note's data.
        """

        form.instance.autor = self.request.user
        form.instance.fecha_modificacion = timezone.now()
        
        # Hacemos lo de calendar
        tarjeta = form.save(commit=False)
        
        
        if not Token.objects.filter(user=self.request.user).exists():
            tarjeta.save()
            return create_credentials()
        
        make_event(form.instance.fecha_vencimiento, form.instance.nombre, request=self.request)
        return super(CrearTarjeta, self).form_valid(form)


class EditarTarjeta(LoginRequiredMixin, UpdateView):
    """Displays a form to edit the note whose ID was passed through
    the URL.

    The user requesting the page has to be the author of the note.
    """

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
    """Deletes a note and all of its history. A confirmation button
    is displayed before performing the actual deletion.

    The user requesting the page has to be the author of the note.
    """

    login_url = '/accounts/login'
    model = Tarjeta
    template_name = 'tarjeta/delete_form.html'
    success_url = reverse_lazy('tarjetas:index')

@login_required(login_url='/accounts/login/')
def download_note(request, tarjeta_id):
    """Requests the note as a markdown file stored in-memory, and
    returns it to the user so it can be downloaded.

    The user requesting the page has to be the author of the note.
    """

    try:
        tarjeta = Tarjeta.objects.get(pk=tarjeta_id)
    except Tarjeta.DoesNotExist:
        raise Http404("La tarjeta no existe o no tienes permisos para accederla.")

    if (not request.user.is_authenticated) or request.user != tarjeta.autor:
        raise Http404("La tarjeta no existe o no tienes permisos para accederla.")

    file_buffer = tarjeta.to_markdown_file()
    file_buffer.seek(0)

    response = FileResponse(file_buffer, as_attachment=True, filename='{}.md'.format(tarjeta.nombre))
    return response
