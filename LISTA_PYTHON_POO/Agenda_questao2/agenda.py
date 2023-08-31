from Agenda_questao2.contato import Contato

class Agenda():

    def __init__(self):
        self.contatos = []

    def salvar_contato(self, contato:Contato):
        self.contatos.append(contato)

    def remover_contato(self, nome_contato):
        contato_existe = False
        for contato in self.contatos:
            if contato.get_nome() == nome_contato:
                contato_existe = True
                self.contatos.remove(contato)
            
        if contato_existe == False:
            print('O contato nao existe')

    def buscar_pessoa(self, contato_nome):
        for contato in self.contatos:
            if contato.get_nome() == contato_nome:
                return(self.contatos.index(contato))

    def imprimir_agenda(self):
        for contato in self.contatos:
            print(contato)

    def detalhar_contato(self, index):
        posicao_valida = range(len(self.contatos))
        if index in posicao_valida:
            print(self.contatos[index])
        
        else:
            print('Posição inválida!')
        
