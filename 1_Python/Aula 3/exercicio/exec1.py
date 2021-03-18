"""
1.	Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura. 
Crie um método para imprimir todos dados de uma pessoa. 
Crie um método para calcular a idade da pessoa
"""
from datetime import datetime

class Pessoa(object):
    __nome = str()
    __data_de_nascimento = datetime.now()
    __altura = float()

    def __init__ (self, nome :str, dt_nascimento : datetime, altura : float):
        self.__nome = nome
        self.__data_de_nascimento = dt_nascimento
        self.__altura = altura

    def getNome(self):
        return self.__nome    

    def printAll(self):
        print(f"Nome {self.__nome}, Data de Nascimento {self.__data_de_nascimento.strftime('%d/%m/%Y')} e Altura {self.__altura}") 

    def calcIdade(self):
        today = datetime.now()
        born = self.__data_de_nascimento
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

if __name__ == '__main__':
    pes = Pessoa("Tiago DAgostino", datetime.strptime("15/08/1981", '%d/%m/%Y'), 2.0) 
    pes.printAll()   
    print(pes.calcIdade())    
