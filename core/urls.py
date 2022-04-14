from django.urls import path, reverse_lazy

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.ListarTarjeta.as_view(), name='index'),
    path('create/', views.CrearTarjeta.as_view(), name='create'),
    # url(r'^edit/(?P<pk>\d+)/$', views.EditarTarjeta.as_view(), name='edit'),
    path('delete/<pk>/', views.EliminarTarjeta.as_view(), name='delete'),
    path('view/<pk>/', views.VerTarjeta.as_view(), name='view'),
]
