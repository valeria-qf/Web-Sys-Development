from django.db import models

class Coordenador(models.Model):
    nome_coordenador = models.CharField(max_length = 200)
    identificador = models.CharField(max_length = 20)
    email_coordenador = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome_coordenador

class Curso(models.Model):
    nome_curso = models.CharField('Nome do curso', max_length = 100)
    coordenador_curso = models.OneToOneField(Coordenador,  on_delete= models.CASCADE)
    
    def __str__(self):
        return self.nome_curso
class Cidade(models.Model):
    nome_cidade = models.CharField('Nome', max_length = 100)
    sigla_estado = models.CharField('Sigla do Estado', max_length = 2)

    def __str__(self):
        return f'{self.nome_cidade} - {self.sigla_estado}'
class Aluno(models.Model):
    nome_aluno = models.CharField('Nome', max_length = 200)
    endereco = models.CharField('Endereço', max_length = 200)
    email_aluno = models.EmailField('Email', max_length = 200)
    data_nascimento = models.DateField('data de nascimento')
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome_aluno

