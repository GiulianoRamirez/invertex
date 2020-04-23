from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from app.models import perfilesDeUsuario, mensajesConfirmacion
from django.core import serializers

def index(request):
    return render(request, 'index.html')
    
def panelAdminConfirmaciones(request):

    usuarios = perfilesDeUsuario.objects.all()

    usuariosJson = serializers.serialize('python',usuarios)
    
    mensajeConfirmacion = mensajesConfirmacion.objects.get(id="1")
    
    return render(request, 'panelAdminConfirmaciones.html', {"mensajeConfirmacion":mensajeConfirmacion.mensaje, "usuarios":usuariosJson})

def register(request):
    return render(request, 'register.html')

def pantallaPostRegistro(request):
    return render(request, 'pantallaPostRegistro.html') 

def login(request):
    return render(request, 'login.html')

def recuperarContrasena(request):
    return render(request, 'recuperarContrasena.html')

def userMain(request):

    return render(request, 'userMain.html')



