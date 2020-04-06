from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import hashlib

import base64
from PIL import Image
from io import BytesIO

from app.models import perfilesDeUsuario



def formularioRegister(request):
    
    nombres = request.POST["nombres"]
    paterno = request.POST["paterno"]
    materno = request.POST["materno"]
    rut = request.POST["rut"]
    digitoVerificador = request.POST["digitoVerificador"]
    correo = request.POST["correo"]
    fechaNacimiento = request.POST["fechaNacimiento"]
    contrasena = request.POST["contrasena"]
    documento = request.FILES["documento"]

    hash_object = hashlib.sha256(contrasena.encode())
    contrasenaHash = hash_object.hexdigest()
    print(contrasenaHash)

    documentoBase64 = ""

    #para imagen png
    try:
        image = Image.open(documento) 
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        documentoBase64 = base64.b64encode(buffered.getvalue())
    except:
        print("La imagen no es .png")
    
    if(documentoBase64 != ""):
        insert = perfilesDeUsuario( nombres=nombres,
                                    apellidoPaterno = paterno,
                                    apellidoMaterno = materno,
                                    fechaNacimiento = fechaNacimiento,
                                    rut = rut,
                                    digitoVerificador = digitoVerificador,
                                    correo = correo,
                                    contrasena= contrasenaHash,
                                    documento = documentoBase64,
                                    origenCuenta = "pagina",
                                    tipoUsuario = "usuario",
                                    estadoConfirmacion = "porConfirmar")

        insert.save()
    
    #return HttpResponse(img_str)
    return render(request, 'pantallaPostRegistro.html' )


    


