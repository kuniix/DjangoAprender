from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cars_view(request):
   
    return render(request,
                  'cars.html',
                  {'cars': {'model': 'Skyline R34'}})

def cars_value(request):
    return HttpResponse("Os carros mais valiosos.")