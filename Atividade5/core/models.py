from django.db import models

class Discos(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=200)
    pais = models.CharField(max_length = 200)
    ano = models.IntegerField()
    genero = models.CharField(max_length = 200)
    quantidade = models.IntegerField()
    