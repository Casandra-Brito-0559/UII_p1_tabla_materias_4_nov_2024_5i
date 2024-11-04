from django.shortcuts import render
from .models import Materias
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materias.objects.all()
    return render(request,'gestionarMaterias.html')