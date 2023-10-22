from django.urls import path
from . import views


urlpatterns = [
    path('reporte/reporte', views.reporte, name = 'reporte'),
    path('reporte/balance', views.balance, name = 'balance_general'),
]