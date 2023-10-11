from django.db import models

class SeloFonografico(models.Model):
    nome = models.CharField(max_length = 200)
    def __str__(self):
        return (f'selo fonográfico: {self.nome}')
class Artista(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return (f'Nome: {self.nome}')

class Discos(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    pais = models.CharField(max_length = 200)
    ano = models.IntegerField()
    genero = models.CharField(max_length = 200)
    quantidade = models.IntegerField()
    selo_fonografico = models.ForeignKey(SeloFonografico, on_delete = models.CASCADE)
    artistas = models.ManyToManyField(Artista)

    def __str__(self):
        todos_artistas = ', '.join([artistas.nome for artistas in self.artistas.all()])
        return (f'Nome: {self.nome}, Artistas: {todos_artistas}, Gênero: {self.genero} selo fonográfico: {self.selo_fonografico}')
