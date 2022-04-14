from django.urls import path, reverse_lazy

from core import views

app_name = 'core'
urlpatterns = [
    # url(r'^$', views.ListarTarjeta.as_view(), name='index'),
    path('create/', views.CrearTarjeta.as_view(), name='create'),
    # url(r'^edit/(?P<pk>\d+)/$', views.EditarTarjeta.as_view(), name='edit'),
    # url(r'^delete/(?P<pk>\d+)/$', views.EliminarTarjeta.as_view(), name='delete'),
    # url(r'^view/(?P<pk>\d+)/$', views.show_post, name='view'),
]
