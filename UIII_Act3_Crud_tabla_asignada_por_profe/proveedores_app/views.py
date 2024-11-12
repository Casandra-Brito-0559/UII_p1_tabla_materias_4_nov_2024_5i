from django.shortcuts import render
from .models import Proveedores
# Create your views here.
def inicio_vista(request):
    losproveedores=Proveedores.objects.all()
    return render(request, 'gestion.html',{'misproveedores':losproveedores})
    
    def registrar(request):
    id = request.POST["txtid"]
    nombre = request.POST["txtnombre"]

    creditos = request.POST["numcreditos"]

    guardarmateria = Proveedores.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')

def seleccionar(request, codigo):
    materia = Proveedores.objects.get(codigo=codigo)
    return render(request, 'editarMateria.html',{'mismaterias':materia})

def editarMateria(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    materia = Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()
    return redirect('/')

def borrarMateria(request, codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    return redirect("/")