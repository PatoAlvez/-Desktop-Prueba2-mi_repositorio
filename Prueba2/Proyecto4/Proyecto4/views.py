from django.http import HttpResponse
from django.template import Template, context


def saludo(request):
    return HttpResponse("Hola Django-Coder")

def segunda_vista(request):
    return HttpResponse("Bienvenidos </br> al Himalaya")

def probandotemplate(self):
    mihtml= open("C:/Users/LTA/Desktop/Prueba2/Proyecto4/Proyecto4/planillas/template1.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= context()
    documento= plantilla.render(micontexto)
    return HttpResponse (documento)
