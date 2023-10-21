from django.urls import path
from . import views

urlpatterns = [
    path('cuenta/cuenta', views.cuentas, name='cuenta'),
    path('cuenta/mostrar_cuentas', views.cuentas_view, name='libro'),
    #---------------- URLS DEL CRUD DEL CATALOGO DE CUENTAS -------------------------------------------------------
    path('cuenta/crud/crear', views.crear.as_view(), name='crear'),
    path('cuenta/crud/modificar/<pk>/', views.modificar.as_view(), name='modificar'),
    path('cuenta/crud/eliminar/<pk>/', views.eliminar.as_view(), name='eliminar'),
    
]
