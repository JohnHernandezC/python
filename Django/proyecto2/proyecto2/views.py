from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):

    #rescatar valores desde python a la plantilla
    #nombre="jhon"
    #apellido="hernandez"
    #"temas":["plantillas","modelos","formularios","vistas","despliegues"]

    p1 = Persona("el john", "hernandez")
    temas = ["plantillas", "modelos", "formularios", "vistas", "despliegues"]
    dame_fecha = datetime.datetime.now()

    #carcar plantilla normal

    doc_externo = open("C:/Users/johnh/Desktop/Django/proyecto2/proyecto2/plantilla.html")
    plt=Template(doc_externo.read())
    ctx = Context({"nombre_persona": p1.nombre , "apellido_persona": p1.apellido, "fecha_actual": dame_fecha,"lista_temas":temas})
    #ctx = Context({"nombre_persona":"Jhon", "apellido_persona":"Hernandez", "fecha_actual":dame_fecha})
    doc_externo.close()
    #documento=plt.render(ctx)
    documento = plt.render(ctx)


    #cargadores

    #doc_externo=loader.get_template('plantilla.html')

    #documento=doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha_actual": dame_fecha,"lista_temas":temas})

    return HttpResponse(documento)



def despedida(request):

    return HttpResponse("GRACIAS Y ADIOS")

def dameFecha(request):

      fecha_actual = datetime.datetime.now()
      documento = """<html>
             <body>
             <h1>
             fecha y horas actuales %s 
             </h1>
             </body>
             </html>""" % fecha_actual
      return HttpResponse(documento)
#al conjunto se le llama plantillas


def calcula_edad(request, agno):

    edad_actual = 21
    periodo = agno-2020
    edadFutura = edad_actual+periodo

    documento1 = "<html><body><h1>en el año %s tendras %s años</h1></body></html>" % (agno, edadFutura)
    return HttpResponse(documento1)
