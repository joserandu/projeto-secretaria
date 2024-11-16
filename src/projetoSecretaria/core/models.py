from django.db import models


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    faltas_seguidas = models.IntegerField("Número de faltas seguidas")
