# Generated by Django 3.0.4 on 2020-04-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensajesConfirmacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=1000)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='perfilesDeUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('rut', models.IntegerField()),
                ('digitoVerificador', models.CharField(max_length=1)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=500)),
                ('documento', models.TextField()),
                ('tipoUsuario', models.CharField(max_length=50)),
                ('estadoConfirmacion', models.CharField(max_length=50)),
                ('origenCuenta', models.CharField(max_length=50)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
