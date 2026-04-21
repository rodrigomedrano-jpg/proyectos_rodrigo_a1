from django.urls import path
from . import views

# Namespace para las URLs de esta app
app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.curso_detalle, name='curso_detalle'),
    path('acerca/', views.acerca, name='acerca'),
    path('productos/', views.prueba, name='prueba'),
]