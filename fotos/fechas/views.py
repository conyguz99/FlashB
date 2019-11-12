from django.shortcuts import render
from .models import Tipo, Reserva, ReservaInstancia
# Create your views here.
def index(request):
    #Contador de las reservas
    num_reservas= Reserva.objects.all().count()
    num_instancias=ReservaInstancia.objects.all().count()
    #Fechas disponibles estado 'd'
    num_instancias_disponibles=ReservaInstancia.objects.filter(status__exact='d').count()
    return render(
        request,
        'index.html',
        context={'num_reservas':num_reservas,'num_instancias':num_instancias,'num_instancias_disponibles':num_instancias_disponibles},
    )