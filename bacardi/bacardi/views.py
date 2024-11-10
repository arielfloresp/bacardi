from django.shortcuts import render, redirect
from core.models import Pais

def step1 (request):
    return render(request, 'core/step1.html')

def step2(request):
    return render(request, 'core/step2.html')

def step2(request):
    return render(request, 'core/step2.html')

def paso1(request):
    return render(request, 'core/paso1')

def seleccion_pais(request):
    paises_america = Pais.objects.filter(continente_id=2)
    print(paises_america)  # Para depuración
    return render(request, 'core/step1.html', {'paises': paises_america})

def formulario_paso1(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        pais_id = request.POST.get('pais_id')
        es_mayor_de_edad = request.POST.get('es_mayor_de_edad') == 'on'

        if es_mayor_de_edad:
            # Si el usuario es mayor de edad, guarda el país en la sesión y redirige al paso 2
            request.session['pais_id'] = pais_id
            return redirect('core/step2')
        else:
            # Si el usuario no es mayor de edad, redirige a Google
            return redirect('https://www.google.com')

    paises = Pais.objects.all()
    return render(request, 'core/paso1.html', {'paises': paises})