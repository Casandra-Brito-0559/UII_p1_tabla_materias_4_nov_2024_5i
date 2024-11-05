from django.shortcuts import render,redirect
from .models import Materias
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materias.objects.all()
    return render(request,'gestionarMaterias.html',{'mismaterias':lasmaterias})

def registrarMaterias(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]

    guardarMateria=Materias.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')