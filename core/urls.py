from django.urls import path, reverse_lazy

from core.views  import tarjeta, error

app_name = 'core'
urlpatterns = [
    path('', tarjeta.ListarTarjeta.as_view(), name='index'),
    path('create/', tarjeta.CrearTarjeta.as_view(), name='create'),
    path('edit/<pk>/', tarjeta.EditarTarjeta.as_view(), name='edit'),
    path('delete/<pk>/', tarjeta.EliminarTarjeta.as_view(), name='delete'),
    path('view/<pk>/', tarjeta.VerTarjeta.as_view(), name='view'),
]
