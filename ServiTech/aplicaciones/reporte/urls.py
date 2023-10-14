from django.urls import path
from . import views

urlpatterns = [
    path('reporte/reporte', views.reporte, name = 'reporte')
]