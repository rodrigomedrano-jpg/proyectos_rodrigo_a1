from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perro/', views.perro),
    path('gato/', views.gato, name='gato'),
]