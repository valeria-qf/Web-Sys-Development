from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField('Nome do cliente', max_length= 200)
    email = models.CharField(max_length= 200)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_cliente

class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()
    def __str__(self):
        return f'AP: {self.apartamento} - R$: {self.valor}'

class Hospedagem(models.Model):
    data_entrada = models.DateField('Data de entrada')
    data_saida = models.DateField('Data de saída')
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete= models.CASCADE)

    def __str__(self):
        return f' Cliente: {self.cliente.nome_cliente} - Entrada: {self.data_entrada}, Saída: {self.data_saida}'

class Consumo(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField('Data')
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem, on_delete= models.CASCADE)

    def __str__(self):
        return f' Cliente: {self.hospedagem.cliente.nome_cliente} - Cunsumido: {self.nome}, Valor: {self.valor}'



    
