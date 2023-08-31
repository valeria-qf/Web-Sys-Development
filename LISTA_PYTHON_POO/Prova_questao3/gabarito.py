class Gabarito():

        def __init__(self):
            self.__respostas_corretas = [None] *15
           
        def preencher_respostas_corretas_gabarito(self, lista_de_respostas_corretas):
            
             if len(lista_de_respostas_corretas) != len(self.__respostas_corretas):
                 print('Número de respostas inválido!\n')

             else:
                self.__respostas_corretas = lista_de_respostas_corretas

        def resposta_questao(self, numero_questao):

            numero_questao_valida = range(len(self.__respostas_corretas))
            if (numero_questao - 1) in numero_questao_valida:
                print('{} - Resposta Correta: {}'.format(numero_questao, self.__respostas_corretas[numero_questao - 1]))
                
            else:
                print('Número da questão inválido!')

        def get_respostas_corretas(self):
             return self.__respostas_corretas
        