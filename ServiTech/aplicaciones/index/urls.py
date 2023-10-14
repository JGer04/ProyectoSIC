from django.urls import path
from . import views

urlpatterns = [
    path('index/index', views.index, name='inicio'),
]
