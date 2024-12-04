from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(model__icontains=search)
    else:
        cars = Car.objects.all()
   
    return render(request,
                  'cars.html',
                  {'cars': cars})

def cars_value(request):
    return HttpResponse("Os carros mais valiosos.")