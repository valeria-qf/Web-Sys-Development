class Contato():

    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def __str__(self):
        return('Nome: {}, Email: {}, Telefone: {}'. format(self.get_nome(), self.get_email(), self.get_telefone()))

# Setters
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    def set_email(self, novo_email):
        self.__email = novo_email

# Getters
    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone
    
    def get_email(self):
        return self.__email
    