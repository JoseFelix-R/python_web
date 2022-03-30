# Arquivo usado para tratar das regras de negocio


from django.db import models
from django.forms import CharField

class Equipamento(models.Model):
    modelo = models.CharField(
        max_length = 255,
        null = False,
        blank= False
    )

    marca = models.CharField(
        max_length = 255,
        null = False,
        blank= False
    )

    tombamento = models.CharField(
        max_length = 12,
        null = False,
        blank= False
    )

    estado = models.TextField(
        max_length = 600,
        null = False,
        blank= False
    )

    status = models.IntegerField(
        default = 0,
        null = False,
        blank= False
    )

    entradasaida= models.CharField(
        max_length = 255,
        null = False,
        blank= False
    )

    objetos = models.Manager()

# Não é necessario atributo ID pois o mesmo é herdado de models

