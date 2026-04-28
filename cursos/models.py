from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique= True,
        verbose_name= 'Nombre de la categoria',
    )
    descripcion = models.TextField(
        blank = True,
        verbose_name= 'Descripción de la categoria'
    )
    slug = models.SlugField(
        max_length= 150,
        unique= True,
        blank = True,
        verbose_name= 'Slug de la categoria'
    )
    creado = models.DateTimeField(auto_now_add= True)
    actualizado = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.nombre.replace(' ', '-').lower()
        super().save(*args, **kwargs)