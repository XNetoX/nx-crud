from django.db import models
from django.forms import CharField
from django.core.validators import MinLengthValidator

# Create your models here.


class Dados(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)
