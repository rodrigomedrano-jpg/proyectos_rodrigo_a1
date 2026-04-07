
from django.urls import path
from . import views

app_name = 'estudiantes'

urlpatterns = [
    path('', views.registro, name='registro'),
    path('lista/', views.lista, name='lista'),
    path('limpiar/', views.limpiar, name='limpiar'),
]