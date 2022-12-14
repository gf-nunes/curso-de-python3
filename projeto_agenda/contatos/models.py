from time import timezone
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
