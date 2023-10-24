from django.urls import path
from . import views

urlpatterns = [
    path('costo/costo', views.reporte, name = 'costo'),
    path('costo/servicio', views.servicio, name = 'servicio'),
    path('costo/actividad', views.TablaActividades, name='actividad'),
    path('costo/costeo', views.costeo, name='costeo'),
]
