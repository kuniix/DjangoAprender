from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cars_view(request):
    return HttpResponse("A view da pagina cars")

def cars_value(request):
    return HttpResponse("Os carros mais valiosos.")