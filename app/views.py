from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import hashlib
import base64
from PIL import Image
from io import BytesIO



import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


import PyPDF2
from pdf2image import convert_from_bytes

from app.models import perfilesDeUsuario, mensajesConfirmacion

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import redirect

import urllib.request



def formularioLogin(request):
    correo = request.POST['correo']
    contrasena = request.POST['contrasena']

    print(correo)
    print(contrasena)

    hash_object = hashlib.sha256(contrasena.encode())
    contrasenaHash = hash_object.hexdigest()

    usuario = perfilesDeUsuario.objects.get(correo=correo)
    
    if(usuario.estadoConfirmacion != "confirmado"):
        return redirect('/login/')

    if(usuario.contrasena == contrasenaHash):
        print("login correcto")
        return render(request, 'userMain.html', {'nombres': usuario.nombres, 'contrasena': usuario.contrasena})
    
    else:
        print("login fallido")
        return redirect('/login/')

@csrf_exempt
def formRecuperarContrasena(request):
    correo = request.POST['correo']
    usuario = perfilesDeUsuario.objects.get(correo=correo)
    contrasenaDecryp = urllib.request.urlopen("https://md5decrypt.net/en/Api/api.php?hash="+usuario.contrasena+"&hash_type=sha256&email=giulianox_2014@hotmail.com&code=aa4e9cda5ec6fa38").read()
    print(contrasenaDecryp)
    aux = list(str(contrasenaDecryp))
    aux[0] = ""
    aux[1] = ""
    aux[-1] = ""
    aux[-2] = ""
    aux[-3] = ""
    print(aux)

    aux2 = ""
    for i in aux:
        print(i)
        aux2 = aux2 + str(i)

    contrasenaDecryp = aux2

    print(contrasenaDecryp)

    print(correo)

    #envio de correo

    message = Mail(
        from_email='hisdfm@yajgf.com',
        to_emails=str(correo),
        subject='recuperacion contrasena',
        html_content='Haz solicitado una recuperacion de contrasena, tu contrasena es: <strong>'+ str(contrasenaDecryp) +'</strong>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)



    return redirect("/login/")

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

    formatosAdmitidos = ["png","pdf","jpg","jpeg"]

    rutFormat = ""
    
    for i in rut:
        if i != ".":
            rutFormat = rutFormat + i
    
    rut = rutFormat


    print(str(documento).split()[-1])

    if( str(documento).split(".")[-1] not in formatosAdmitidos):
        return render(request, 'pantallaPostRegistro.html', {"mensaje1":"Registro fallido" ,"mensaje2":"Ingresa un formato de archivo valido (png, jpg, jpeg o pdf)"})

    hash_object = hashlib.sha256(contrasena.encode())
    contrasenaHash = hash_object.hexdigest()
    print(contrasenaHash)

    documentoBase64 = ""

    

    
    #envio de correo
    SENDGRID_API_KEY='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'
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
    #-------------------------------------------------

    #para imagen png, jpg o jpeg
    try:
        image = Image.open(documento) 
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        documentoBase64 = base64.b64encode(buffered.getvalue())
    except:
        print("imagen png fallido")

    
    #-------------------------------------------------


    #para pdf
    try:
        tmp = BytesIO()
        output = PyPDF2.PdfFileWriter()
        pdfOne  = PyPDF2.PdfFileReader(documento)
        for page in range(pdfOne.getNumPages()):
            output.addPage(pdfOne.getPage(page))

        output.write(tmp)
        images = convert_from_bytes(tmp.getvalue())
        image = images[0]
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        documentoBase64 = base64.b64encode(buffered.getvalue())
    except:
        print("imagen pdf fallido")

    



    if(documentoBase64 != ""):
        documentoBase64 = str(documentoBase64)
        documentoBase64 = documentoBase64.replace("b","",1)
        documentoBase64 = documentoBase64.replace("'","",1)
        documentoBase64 = documentoBase64.replace("'","",-1)


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

    
    



    #return HttpResponse(documentoBase64)
    return render(request, 'pantallaPostRegistro.html', {"mensaje1":"Registro exitoso!" ,"mensaje2":"(Espera a tu confirmación por correo)"})

@csrf_exempt
def confirmacionRegister(request):

    nombres = request.GET["nombres"]
    correo = request.GET["correo"]
    mensajeConfirmacion = mensajesConfirmacion.objects.get(id="1")

    print("SE ENVIAAAAAAAAAA")
    

    #envio de correo
    SENDGRID_API_KEY='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'
    message = Mail(
    from_email='informacion@invertex.cl',
    to_emails=correo,
    subject='Registro Confirmado Invertex' + nombres,
    html_content='<h1>Saludos '+nombres+ '</h1> <br>'+ mensajeConfirmacion.mensaje) 


    try:
        usuario = perfilesDeUsuario.objects.get(correo=correo)
        usuario.estadoConfirmacion = "confirmado"
        usuario.save()
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
        
    except:
        print("no se envia correo")


    return HttpResponse(nombres)

@csrf_exempt
def rechazoRegister(request):

    nombres = request.POST["nombres"]
    correo = request.POST["correo"]
    mensaje = request.POST["mensaje"]
    

    print("SE ENVIAAAAAAAAAA rechazoo")

    print("\n=================================\n")
    print(mensaje)
    print("\n=================================\n")
    

    #envio de correo
    SENDGRID_API_KEY='SG._fJTxtasTEujjm_qfO-6uA.moMSz4DbaQfq41JgSjwwzBcB6oGNbsRhJlXnjopr_a4w'
    message = Mail(
    from_email='informacion@invertex.cl',
    to_emails=correo,
    subject='Registro Rechazado Invertex',
    html_content='<h5>Saludos '+nombres+ '</h5> <br><br>'+ mensaje)

    try:
        usuario = perfilesDeUsuario.objects.get(correo=correo)
        usuario.estadoConfirmacion = "rechazado"
        usuario.save()
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        

    except:
        print("no se envia correo")


    return HttpResponse(nombres)

@csrf_exempt
def cambiarMensajeConfirmacion(request):
    mensaje = request.POST["mensaje"]
    print("ACAAAAAAAAA")
    print(mensaje)
    mensajeConfirmacion = mensajesConfirmacion.objects.get(id="1")
    mensajeConfirmacion.mensaje = mensaje
    mensajeConfirmacion.save()

    return HttpResponse(mensaje)

@csrf_exempt
def verMensajeConfirmacion(Request):
    mensajeConfirmacion = mensajesConfirmacion.objects.get(id="1")
    return HttpResponse(mensajeConfirmacion.mensaje)

