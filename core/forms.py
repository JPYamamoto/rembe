from django import forms
from markdownx.fields import MarkdownxFormField

from core.models.tarjeta import Tarjeta

class TarjetaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    fecha_vencimiento = forms.DateTimeField(label='Fecha de Vencimiento', required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'))
    contenido = MarkdownxFormField(label='Contenido', required=True)
    contenido_reverso = MarkdownxFormField(label='Contenido Reverso', required=False)
    tema = forms.ChoiceField(label='Tema', required=True, choices=Tarjeta.Tema.choices)

    class Meta:
        model = Tarjeta

        fields = [
            'nombre',
            'fecha_vencimiento',
            'contenido',
            'contenido_reverso',
            'tema',
        ]
