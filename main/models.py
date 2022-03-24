from django.db import models

class Participantes(models.Model):
    nome = models.CharField(max_length=255)
    pontuacao = models.IntegerField(default=0)
