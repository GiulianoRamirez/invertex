from django.db import models

class perfilesDeUsuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    rut = models.IntegerField()
    digitoVerificador = models.CharField(max_length=1)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=500)
    documento = models.TextField()
    tipoUsuario = models.CharField(max_length=50)
    estadoConfirmacion = models.CharField(max_length=50)
    origenCuenta = models.CharField(max_length=50)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)



class mensajesConfirmacion(models.Model):
    mensaje = models.CharField(max_length=1000) 
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)



