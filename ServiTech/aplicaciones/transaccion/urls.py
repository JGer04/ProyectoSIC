from django.urls import path
from . import views

urlpatterns = [
    path('transaccion/transaccion', views.index, name='transaccion'),
]