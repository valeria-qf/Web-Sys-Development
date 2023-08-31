from Prova_questao3.gabarito import Gabarito

class Prova():
    
    def __init__(self, gabarito:Gabarito, nome_aluno, nota, acertos):
        self.__gabarito = gabarito
        self.__respostas_aluno = []
        self.__nome_aluno = nome_aluno
        self.__nota = nota
        self.__acertos = acertos
        
    def resposta_aluno(self, resposta_do_aluno):
        tamanho_prova = 15
        tamanho_lista_respostas_corretas = len(self.__respostas_aluno)
    
        if tamanho_lista_respostas_corretas < tamanho_prova:
            self.__respostas_aluno.append(resposta_do_aluno)

        elif tamanho_lista_respostas_corretas > tamanho_prova:
            print('O gabarito de respostas já está completo!')

        return self.__respostas_aluno

    def acertos_prova(self):
        pontuacao_dez_primeiras = 0.5
        pontuacao_cinco_ultimas = 1
        self.__acertos = 0
        self.__nota = 0
        respostas_corretas = self.__gabarito.get_respostas_corretas()

        for index in range(len(self.__respostas_aluno)):
            resposta_aluno = self.__respostas_aluno[index]
            resposta_correta = respostas_corretas[index]

            if  resposta_aluno == resposta_correta :
                self.__acertos += 1

                if index < 10:
                    self.__nota += pontuacao_dez_primeiras

                else:
                    self.__nota += pontuacao_cinco_ultimas

        return ('Total de acertos: {}'.format(self.__acertos))

    def nota(self):

        self.acertos_prova()
        return ('{} - nota: {}'.format(self.__nome_aluno, self.__nota))
        
    def maior_nota(self, prova):
        if self.__nota > prova.get_nota():
            print('\n-------------------------------------------\nMaior Nota: \n{} - {}\n-------------------------------------------\n'.format(self.__nome_aluno, self.__nota))
        
        elif self.__nota == prova.get_nota():
            print('\n-------------------------------------------\nNotas Iguais!  \n{} - {}  \n{} - {}\n-------------------------------------------\n'.format(self.__nome_aluno, self.__nota, prova.get_nome_aluno(), prova.get_nota()))
        
        else:
             print('\n-------------------------------------------\nMaior Nota: \n{} - {}\n-------------------------------------------\n'.format(prova.get_nome_aluno(), prova.get_nota()))

    def get_nome_aluno(self):
        return self.__nome_aluno
    
    def get_nota(self):
        return self.__nota

    def get_gabarito(self):
        return self.__gabarito.get_respostas_corretas()

