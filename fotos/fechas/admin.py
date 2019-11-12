from django.contrib import admin

from . models import Tipo, Reserva, ReservaInstancia

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Reserva)
admin.site.register(ReservaInstancia)
