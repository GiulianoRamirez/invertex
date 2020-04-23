"""invertex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invertex.views import index,register, panelAdminConfirmaciones, login, pantallaPostRegistro, userMain, recuperarContrasena
from app.views import formularioRegister, confirmacionRegister, rechazoRegister, cambiarMensajeConfirmacion, verMensajeConfirmacion, formularioLogin, formRecuperarContrasena


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('register/', register),
    path('pantallaPostRegistro/', pantallaPostRegistro),
    path('confirmaciones/', panelAdminConfirmaciones),
    path('login/', login),
    path('recuperarContrasena/', recuperarContrasena),
    path('formRecuperarContrasena/', formRecuperarContrasena),
    path('formularioLogin/', formularioLogin),
    path('formularioRegister/', formularioRegister),
    path('confirmacionRegister/', confirmacionRegister),
    path('rechazarRegister/', rechazoRegister),
    path('cambiarMensajeConfirmacion/', cambiarMensajeConfirmacion),
    path('verMensajeConfirmacion/', verMensajeConfirmacion),
    path('main/', userMain),
    path('', index),
]

