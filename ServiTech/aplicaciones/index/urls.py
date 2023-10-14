from django.urls import path
from . import views

urlpatterns = [
    path('index/index', views.index, name='inicio'),
    path('index/index2', views.index2, name='inicio2'),
]
