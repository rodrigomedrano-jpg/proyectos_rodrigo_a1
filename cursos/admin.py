from django.contrib import admin
from .models import Categoria
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','slug','creado')
    search_fields = ('nombre',)