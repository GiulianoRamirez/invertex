from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import hashlib

import base64
from PIL import Image
from io import BytesIO

from app.models import perfilesDeUsuario

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



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

    SENDGRID_API_KEY='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'

    
    #envio de correo
    message = Mail(
    from_email='informacion@invertex.cl',
    to_emails=correo,
    subject='Registro invertex',
    html_content='Gracias por registrarte en Invertex, su cuenta esta en proceso de validación, le enviaremos un correo una vez su cuenta sea validada')

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except:
        print("no se envia correo")

    #para imagen png, jpg, jpeg
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


    


