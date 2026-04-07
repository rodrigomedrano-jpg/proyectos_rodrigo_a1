from django.shortcuts import redirect, render

# Create your views here.
def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre','').strip()
        email = request.POST.get('email','').strip()
        edad = request.POST.get('edad','').strip()
        carrera = request.POST.get('carrera','').strip()
        
        errores = []
        
        if not nombre:
            errores.append("El nombre es obligatorio.")
        elif len(nombre) < 3:
            errores.append("El nombre debe tener al menos 3 caracteres.")
            
        if not email:
            errores.append("El email es obligatorio.")
        elif '@' not in email or '.' not in email:
            errores.append("El email no es válido.")
        
        if not edad:
            errores.append("La edad es obligatoria.")
        else:
            try:
                edad_num = int(edad)
                if edad_num < 15 or edad_num > 150:
                    errores.append("La edad debe estar entre 15 y 150 años.")
            except ValueError:
                errores.append("La edad debe ser un número entero.")
        if not carrera:
            errores.append("Debes seleccionar una carrera ")
            
        if errores:
            contexto = {
                'errores': errores,
                'datos': {
                    'nombre': nombre,
                    'email': email,
                    'edad': int(edad),
                    'carrera': carrera
                }
            }
            return render(request, 'estudiantes/registro.html', contexto)
        
        if 'estudiantes' not in request.session:
            request.session['estudiantes'] = []
        
        estudiante ={
            'nombre': nombre,
            'email': email,
            'edad': int(edad),
            'carrera': carrera
        }
            
        request.session['estudiantes'].append(estudiante)
        request.session.modified = True
            
        return redirect('estudiantes:lista')
    contexto={
        'datos': {
            'telefono': '7123457'
        }
    }
    return render(request, 'estudiantes/registro.html', contexto)

def lista(request):
    
    estudiantes =request.session.get('estudiantes', [])
    
    stats = {
        'programacion': 0,
        'diseno' : 0,
        'marketing': 0,
        'datos': 0
    }
    
    for estudiante in estudiantes:
        carrera = estudiante.get('carrera')
        if carrera in stats:
            stats[carrera] += 1
    
    contexto = {
        'estudiantes': estudiantes,
        'stats': stats,
        'total_estudiantes': len(estudiantes)
    }
    
    return render(request, 'estudiantes/lista.html', contexto)

def limpiar(request):
    if 'estudiantes' in request.session:
        del request.session['estudiantes']
    
    return redirect('estudiantes:lista')