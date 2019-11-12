from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Tipo(models.Model):
    # Model representing a book genre."""
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Código único de reserva')
    nombrecompleto = models.CharField(max_length=500, help_text='Escribe tu nombre completo')
    descripcion = models.TextField(max_length=1000, help_text='agrega una breve descripción de tu sesión')
    fecha_reserva = models.DateField(null=True, blank=True)
    tipo = models.ManyToManyField(Tipo)


    def __str__(self):
        return self.nombrecompleto

    def get_absolute_url(self):
        """Devuelve la url que da acceso a la informacion de la reserva"""
        return reverse('detalles-reserva', args=[str(self.id)])

class ReservaInstancia(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Código único de reserva')
    #fecha_reserva = models.DateField(null=True, blank=True)
    reserva = models.ForeignKey('Reserva', on_delete=models.SET_NULL, null=True)

    ESTADO_RESERVA = (
        ('r', 'Reservado'),
        ('d', 'Disponible'),
        
    )

    estado = models.CharField(
        max_length = 1,
        choices = ESTADO_RESERVA,
        blank = True,
        default ='d',
        help_text = 'Disponible',
    )
    class Meta:
        ordering = ['estado']

    def __str__(self):
        return f'{self.id} ({self.Reserva.nombrecompleto})'


    
