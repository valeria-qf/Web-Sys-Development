from Agenda_questao2.agenda import Agenda
from Agenda_questao2.contato import Contato
from Elevador_questao1.elevador import Elevador
from Prova_questao3.gabarito import Gabarito
from Prova_questao3.prova import Prova


print('\n------------------------------------------------------\nELEVADOR\n------------------------------------------------------\n')
elevador1 = Elevador(int(input('Capacidade do elevador: ')), int(input('Total de andares: ')), pessoas_no_elevador = 4, andar_atual = 0)
elevador1.Sair()
elevador1.Entrar()
elevador1.Entrar()
elevador1.Subir()
elevador1.Subir()
elevador1.Descer()
elevador1.Descer()
elevador1.Descer()

print('\n------------------------------------------------------\nAGENDA\n------------------------------------------------------\n')

valeria = Contato(nome = 'valéria', email = 'vvqf2016@gmail.com', telefone = 999999)
karla = Contato(nome = 'karla', email = 'karlajulyana@gmail.com', telefone = 999989)
dan = Contato(nome = 'Dan', email = 'Dan@gmail.com', telefone = 899989)

agenda = Agenda()
agenda.salvar_contato(valeria)
agenda.salvar_contato(karla)
print('\n-----------------------------------------------------------\n')
agenda.imprimir_agenda()
print('\n-----------------------------------------------------------\n')
posicao_pessoa = agenda.buscar_pessoa('karla')
print(posicao_pessoa)
print('\n-----------------------------------------------------------\n')
agenda.remover_contato('valéria')
agenda.imprimir_agenda()
print('\n-----------------------------------------------------------\n')
agenda.salvar_contato(dan)
agenda.imprimir_agenda()
print('\n-----------------------------------------------------------\n')
agenda.detalhar_contato(0)
agenda.detalhar_contato(5)
agenda.remover_contato('aaa')


print('\n------------------------------------------------------\nPROVA\n------------------------------------------------------\n')
gabarito = Gabarito()
respostas_corretas = ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'C']
gabarito.preencher_respostas_corretas_gabarito(respostas_corretas)
print('\n-------------------------------------------\nPROVA 1\n-------------------------------------------\n')
prova1 = Prova(nome_aluno = 'irlan', gabarito = gabarito, nota = 0, acertos = 0)
respostas_aluno_1 = ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'A']

for resposta_aluno_1 in respostas_aluno_1:
    prova1.resposta_aluno(resposta_do_aluno = resposta_aluno_1)

acertos = prova1.acertos_prova()
print(acertos)
nota_prova1 = prova1.nota()
print(nota_prova1)

print('\n-------------------------------------------\nPROVA 2\n-------------------------------------------\n')
prova2 = Prova(nome_aluno = 'aluisio', gabarito = gabarito, nota = 0, acertos = 0)
respostas_aluno_2 = ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'C', 'A', 'D', 'B', 'E', 'C']

for resposta_aluno_2 in respostas_aluno_2:
    prova2.resposta_aluno(resposta_do_aluno = resposta_aluno_2)

acertos_2 = prova2.acertos_prova()
print(acertos_2)
nota_prova2 = prova2.nota()
print(nota_prova2)

#Verifica qual a maior nota
prova2.maior_nota(prova1)

print('-------------------------------------------\n')
gabarito.resposta_questao(1)
gabarito.resposta_questao(2)
gabarito.resposta_questao(14)
gabarito.resposta_questao(15)
gabarito.resposta_questao(16)
print('\n-------------------------------------------\n')