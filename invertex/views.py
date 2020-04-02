from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

    
def panelAdminConfirmaciones(request):
    return render(request, 'panelAdminConfirmaciones.html')
    


def register(request):
    adades = range(18,101)
    return render(request, 'register.html',{"edades": adades})


def login(request):
    return render(request, 'login.html')



