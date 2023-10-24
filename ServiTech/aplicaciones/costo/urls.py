from django.urls import path
from . import views

urlpatterns = [
    path('costo/costo', views.reporte, name = 'costo'),
    path('costo/servicio', views.servicio, name = 'servicio'),
    path('costo/actividad', views.TablaActividades, name='actividad'),
    path('costo/costeo', views.costeo, name='costeo'),

    path('costo/CRUD-actividad/crear', views.crearAC.as_view(), name='crearAC'),
    path('costo/CRUD-actividad/modificar/<pk>/', views.modificarAC.as_view(), name='modificarAC'),

    path('costo/CRUD-inductor/crear', views.crearIN.as_view(), name='crearIN'),
    path('costo/CRUD-inductor/modificar/<pk>/', views.modificarIN.as_view(), name='modificarIN'),

    path('costo/CRUD-CI/crear', views.crearCI.as_view(), name='crearCI'),
    path('costo/CRUD-CI/modificar/<pk>/', views.modificarCI.as_view(), name='modificarCI'),

    path('costo/CRUD-puesto/crear', views.crearPU.as_view(), name='crearPU'),
    path('costo/CRUD-puesto/modificar/<pk>/', views.modificarPU.as_view(), name='modificarPU'),
]
