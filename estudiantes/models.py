from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='estudiante')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='estudiantes')
    fecha_ingreso = models.DateField(
        auto_now_add=True
    )
    materias = models.ManyToManyField(
        Materia, through='Inscripcion', related_name='estudiantes'
    )
    def __str__(self):
        return self.user.get_full_name()

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    class Meta:
        unique_together = ('estudiante', 'materia')
    
    def __str__(self):
        return f"{self.estudiante} - {self.materia}"