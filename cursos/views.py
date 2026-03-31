from django.shortcuts import render
from datetime import datetime

# Create your views here.
# Vista de inicio
def index(request):
    """Página de inicio del LMS"""
    contexto = {
        'total_cursos': 4,
        'total_estudiantes': 1250,
        'total_instructores': 12,
    }
    return render(request, 'cursos/index.html', contexto)


# Vista de lista de cursos
def lista_cursos(request):
    """Lista todos los cursos disponibles"""
    # Datos de ejemplo (más adelante vendrán de la base de datos)
    cursos = [
        {
            'id': 1,
            'titulo': 'Python desde Cero',
            'instructor': 'Ana García',
            'duracion': '8 semanas',
            'descripcion': 'Aprende Python desde lo básico hasta nivel intermedio',
            'imagen': 'cursos/img/python.jpg'
        },
        {
            'id': 2,
            'titulo': 'Django Avanzado',
            'instructor': 'Carlos Mendoza',
            'duracion': '10 semanas',
            'descripcion': 'Desarrollo web profesional con Django',
            'imagen': 'cursos/img/django.jpg'
        },
        {
            'id': 3,
            'titulo': 'JavaScript Moderno',
            'instructor': 'Laura Pérez',
            'duracion': '6 semanas',
            'descripcion': 'ES6+, async/await y programación funcional',
            'imagen': 'cursos/img/javascript.jpg'
        },
        {
            'id': 4,
            'titulo': 'React para Principiantes',
            'instructor': 'Miguel Torres',
            'duracion': '7 semanas',
            'descripcion': 'Crea aplicaciones web interactivas con React',
            'imagen': 'cursos/img/react.jpg'
        },
    ]
    
    contexto = {
        'cursos': cursos,
        'total': len(cursos)
    }
    return render(request, 'cursos/cursos.html', contexto)


# Vista de detalle de curso
def curso_detalle(request, curso_id):
    """Muestra el detalle de un curso específico"""
    # Simulamos obtener un curso (más adelante será de la BD)
    cursos_data = {
        1: {
            'titulo': 'Python desde Cero',
            'instructor': 'Ana García',
            'duracion': '8 semanas',
            'descripcion': 'Aprende Python desde lo básico hasta nivel intermedio. Este curso te llevará desde la instalación de Python hasta la programación orientada a objetos.',
            'imagen': 'cursos/img/python.jpg',
            'modulos': [
                'Introducción y configuración del entorno',
                'Variables, tipos de datos y operadores',
                'Estructuras de control',
                'Funciones y módulos',
                'Estructuras de datos',
                'Programación orientada a objetos',
                'Manejo de archivos y excepciones',
                'Proyecto final',
            ]
        },
        2: {
            'titulo': 'Django Avanzado',
            'instructor': 'Carlos Mendoza',
            'duracion': '10 semanas',
            'descripcion': 'Desarrollo web profesional con Django. Aprende a crear aplicaciones web escalables y seguras.',
            'imagen': 'cursos/img/django.jpg',
            'modulos': [
                'Arquitectura MVT de Django',
                'Modelos y ORM avanzado',
                'Vistas basadas en clases',
                'Templates y sistema de plantillas',
                'Formularios y validación',
                'Autenticación y autorización',
                'REST APIs con Django REST Framework',
                'Deployment y producción',
            ]
        },
        # Agregar datos para cursos 3 y 4...
    }
    
    curso = cursos_data.get(curso_id, cursos_data[1])
    
    contexto = {
        'curso': curso
    }
    return render(request, 'cursos/curso_detalle.html', contexto)


# Vista Acerca de
def acerca(request):
    """Página acerca de nosotros"""
    contexto = {
        'mision': 'Democratizar la educación en tecnología',
        'vision': 'Ser la plataforma líder en educación en línea',
    }
    return render(request, 'cursos/acerca.html', contexto)

def prueba(request):
    contexto = {
        'nombre': 'Rodrigo',
        'biografia': 'ESTE ES UN EJEMPLO LARGO PARA MOSTRAR TEXTO Y CORTAR EN LA EJECUCIÓN DE MI TEMPLATE',
        'edad': 17,
        'es_premium': True,
        'habilidades': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
        'fecha_registro': datetime.now(),
        'seguidores': 1520,
        'web_personal': None
    }
    return render(request, 'cursos/prueba.html', contexto)