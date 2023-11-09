from django.db import models

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length = 200)
    sigla_estado = models.CharField(max_length = 2)
    def __str__(self):
        return f'{self.nome_cidade}, {self.sigla_estado}'

class Curso(models.Model):
    nome_curso = models.CharField(max_length = 200)
    def __str__(self):
        return f'{self.nome_curso}'
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length = 200)
    endereco = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.nome_aluno}'