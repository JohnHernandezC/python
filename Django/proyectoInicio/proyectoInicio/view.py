from cgitb import html
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader #para metodo 1
from django.shortcuts import render #para metodo 2

class Personas(object):
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido =apellido

def saludo(request):
   p1=Personas("aqui va un nombre que esta en mayuscula 2","y aqui va un apelllido 2")
   nombre="john"
   apellido="hernandez"
   temas=["bogota","medellin","cali","pereira","caldas"]
   fecha_actual= datetime.datetime.now()
   #------------------------------------------cargar plantillas1
   #edadFuturedoc_externo=loader.get_template('plantilla.html')#con esto puedo cargar cualquier plantilla
   #ctx=Context({"nombre_persona":"john", "apellido_personas":"hernandez Chaparro"})
   #documento=doc_externo.render({ "nombre_persona":nombre, "apellido_personas":apellido, "fecha":fecha_actual, "segundo_nombre":p1.nombre, 
   #             "segundo_apellido":p1.apellido, "ciudades":temas })
   #return HttpResponse (documento)
#---------------------------------------------cargar plantillas2
   return render(request, 'plantilla.html',{ "nombre_persona":nombre, "apellido_personas":apellido, "fecha":fecha_actual, "segundo_nombre":p1.nombre, 
                "segundo_apellido":p1.apellido, "ciudades":temas })



def bye(request):
    return HttpResponse ("bye")

def horas(request):
    fecha_actual= datetime.datetime.now()
    fecha="""
    <html>
    <body>
    <h1>
    hora y fecha actual %s
    </h1>
    </body>
    </html>
     """% fecha_actual
    return HttpResponse (fecha)

def edad(request, edadA, age):
    #edadActual=22
    periodo=age - 2022
    #edadFuture=edadActual+periodo
    edadFuture=edadA+periodo
    document="""
    <html>
    <body>
    <h1>
    En el año %s su edad sera de %s
    </h1>
    </body>
    </html> 
     """ % (age,edadFuture)
    return HttpResponse (document)
def herencia_ejemplo(request):
    fecha_actual= datetime.datetime.now()
    return render(request, 'cursoHerencia.html',{"dameFecha":fecha_actual})
def herencia_ejemplo2(request):
    fecha_actual= datetime.datetime.now()
    return render(request, 'curso_herencia2.html',{"dameFecha":fecha_actual})
     
     
