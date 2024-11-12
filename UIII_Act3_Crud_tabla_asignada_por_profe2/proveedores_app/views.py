from django.shortcuts import render
from .models import Proveedores
# Create your views here.
def inicio_vista(request):
    losproveedores=Proveedores.objects.all()
    return render(request, 'gestion.html',{'misproveedores':losproveedores})
    
def registrar(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    gerente = request.POST["txtgerente"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["txtfecha"]

    guardarmateria = Proveedores.objects.create(codigo=codigo,nombre=nombre,telefono=telefono,correo=correo,gerente=gerente,cantidad=cantidad,fecha=fecha)
    return redirect('/')

def seleccionar(request, codigo):
    proveedor = Proveedores.objects.get(codigo=codigo)
    return render(request, 'editar.html',{'misproveedores':proveedor})

def editarMateria(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    gerente = request.POST["txtgerente"]
    cantidad = request.POST["numcantidad"]
    fecha = request.POST["txtfecha"]

    materia = Proveedores.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.telefono=telefono
    materia.correo=correo
    materia.gerente=gerente
    materia.cantidad=cantidad
    materia.fecha=fecha
    materia.save()
    return redirect('/')

def borrarMateria(request, codigo):
    materia=Proveedores.objects.get(codigo=codigo)
    materia.delete()
    return redirect("/")