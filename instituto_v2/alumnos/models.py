"""
models.py — Modelos de la app alumnos.

Un modelo en Django es una clase Python que representa una tabla
en la base de datos. Django se encarga de crear y modificar la
tabla con las migraciones: nunca escribimos SQL a mano para esto.
"""

from django.db import models
from django.utils import timezone #Permite obtener la fecha y hora actual adaptada a la configuración regional

class Alumno(models.Model):
    """
    Representa un alumno del Instituto Superior del Milagro.
    """

    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )

    apellido = models.CharField(
        max_length=100,
        verbose_name='Apellido'
    )

    # unique=True: no pueden existir dos alumnos con el mismo email.
    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico'
    )

    # unique=True: legajo irrepetible.
    legajo = models.IntegerField(
        unique=True,
        verbose_name='Legajo'
    )

    activo = models.BooleanField(
        default=True,
        verbose_name='¿Activo?'
    )

    # auto_now_add=True: Django llena este campo automáticamente
    # con la fecha y hora en que se crea el registro.
    fecha_alta = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de alta'
    )

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        """
        Representación legible del objeto. Django la usa en el panel
        de administración y en los templates con {{ alumno }}.
        """
        return f'{self.apellido}, {self.nombre} (Legajo: {self.legajo})'

    def nombre_completo(self):
        """Método auxiliar que devuelve el nombre completo."""
        return f'{self.nombre} {self.apellido}'
 
class Asistencia(models.Model):
    ESTADO_CHOICES = [
        ('PRESENTE', 'Presente'),
        ('AUSENTE', 'Ausente'),
        ('TARDANZA', 'Tardanza'),
    ]

    alumno = models.ForeignKey(
        Alumno, 
        on_delete=models.CASCADE, 
        related_name='asistencias',
        verbose_name='Alumno'
    )
    fecha = models.DateField( #Almacena datos de tipo fecha
        verbose_name='Fecha de asistencia'
    )
    estado = models.CharField(
        max_length=10, 
        choices=ESTADO_CHOICES, #Muestra la lista, como opciones
        default='PRESENTE',
        verbose_name='Estado'
    )
    observaciones = models.TextField( #Campo para agregar texto
        blank=True, 
        null=True,
        verbose_name='Observaciones / Justificativo'
    )

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        unique_together = ('alumno', 'fecha')#Evita duplicar asistencia del mismo alumno el mismo día
        ordering = ['-fecha', 'alumno__apellido']

    def __str__(self):
        return f"{self.alumno.apellido}, {self.alumno.nombre} - {self.fecha} ({self.estado})"
