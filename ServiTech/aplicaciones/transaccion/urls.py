from django.urls import path
from . import views


urlpatterns = [
    path('transaccion/transaccion', views.TablaTransaccion, name='transaccion'),
    path('transaccion/ingresar_transaccion', views.ingresar_transaccion, name='ingresar_transaccion'),
]