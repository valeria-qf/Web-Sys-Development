class Elevador():
    def __init__(self, capacidade_elevador, total_andares, pessoas_no_elevador, andar_atual):
        self.__capacidade_elevador = capacidade_elevador
        self.__total_andares = total_andares
        self.__pessoas_no_elevador = pessoas_no_elevador
        self.__andar_atual = andar_atual
    
    def Entrar(self):
        if self.__pessoas_no_elevador < self.__capacidade_elevador:
            self.__pessoas_no_elevador += 1
            print('1 pessoa entrou. \nPessoas no elevador: {}\n'.format(self.__pessoas_no_elevador))
        
        else:
            print('Capacidade Máxima Atingida! \n{} pessoas'.format(self.__pessoas_no_elevador))

    def Sair(self):
        if self.__pessoas_no_elevador > 0:
            self.__pessoas_no_elevador -= 1
            print('1 pessoa saiu. \nPessoas no elevador: {}\n'.format(self.__pessoas_no_elevador))
        else:
            print('\nNão tem ninguém no elevador!')
    
    def Subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print('Subir de andar. \nAndar Atual: {}\n'.format(self.__andar_atual))

        else:
            print('Você já está no último andar! \n{} andar'.format(self.__andar_atual))

    def Descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            print('Descer de andar. \nAndar Atual: {}'.format(self.__andar_atual))
        else:
            print('\nVocê já está no térreo!')

    # Setters
    def set_capacidade_elevador(self, novo_capacidade_elevador):
        self.__capacidade_elevador = novo_capacidade_elevador
    
    def set_total_andares(self, novo_total_andares):
        self.__total_andares = novo_total_andares

    def set_pessoas_no_elevador(self, novo_pessoas_no_elevador):
        self.__pessoas_no_elevador = novo_pessoas_no_elevador
    
    def set_andar_atual(self, novo_andar_atual):
        self.__andar_atual = novo_andar_atual


    # Getters
    def get_capacidade_elevador(self):
        return self.__capacidade_elevador

    def get_total_andares(self):
        return self.__total_andares

    def get_pessoas_no_elevador(self):
        return self.__pessoas_no_elevador
    
    def get_andar_atual(self):
        return self.__andar_atual
    
    



    
    