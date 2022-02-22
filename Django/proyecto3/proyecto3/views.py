from django.http import HttpResponse


def saludo(request):

 return HttpResponse("hola putos esta es la primera pagina")

def despedida(request):

 return HttpResponse("adios putos")
