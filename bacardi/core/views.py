from django.shortcuts import render
from .models import Pais

def seleccion_pais(request):
    paises_america = Pais.objects.filter(continente_id=2)
    print(paises_america)  # Para depuración
    return render(request, 'core/step1', {'paises': paises_america})


def step1 (request):
    return render(request, 'core/step1.html')

def step2(request):
    return render(request, 'core/step2.html')
