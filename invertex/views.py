from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def panelAdminConfirmaciones(request):
    return render(request, 'panelAdminConfirmaciones.html')
    
def register(request):
    return render(request, 'register.html')

def pantallaPostRegistro(request):
    return render(request, 'pantallaPostRegistro.html') 

def login(request):
    return render(request, 'login.html')



