from django import forms

from core.models import Tarjeta

class TarjetaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    fecha_vencimiento = forms.DateTimeField(label="Fecha de Vencimiento", required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    contenido = forms.CharField(label='Contenido', required=True, widget=forms.Textarea())
    contenido_reverso = forms.CharField(label='Contenido Reverso', required=False, widget=forms.Textarea())

    class Meta:
        model = Tarjeta

        fields = [
            'nombre',
            'fecha_vencimiento',
            'contenido',
            'contenido_reverso',
        ]
