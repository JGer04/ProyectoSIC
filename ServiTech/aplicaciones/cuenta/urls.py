from django.urls import path
from . import views

urlpatterns = [
    path('cuenta/cuenta', views.cuentas, name='cuenta'),
    
]
