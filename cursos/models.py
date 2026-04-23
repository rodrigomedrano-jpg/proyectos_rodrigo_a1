from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique= True,
        verbose_name= 'Nombre de la categoria',
    )