"""
2.	Crie uma classe Agenda que pode armazenar 10 pessoas e que seja capaz de realizar as seguintes operações:
a.	armazenaPessoa(String nome, int idade, float altura)
b.	removePessoa(String nome)
c.	buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
d.	imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
e.	imprimePessoa(int index); // imprime os dados da pessoa que está na posição “i” da agenda.
"""
import exec1
from datetime import datetime

class Agenda(object):
    __agenda = []

    def armazenaPessoa(self, nome : str, idade : int, altura : float):
        ano_nasc = datetime.now().year - idade -1
        dia_mes = datetime.now().strftime('%d/%m/')
        dt_nasc = datetime.strptime(dia_mes + str(ano_nasc), '%d/%m/%Y')
        pes = exec1.Pessoa(nome, dt_nasc, altura)
        self.__agenda.append(pes)

    def buscaPessoa(self, nome : str):
        cont = 0
        for x in self.__agenda:
            if x.getNome() == nome:
                return cont
            cont += 1
        return -1

    def removePessoa(self, nome : str):
        pos = self.buscaPessoa(nome)
        if (pos != -1):
            self.__agenda.pop(pos)

    def imprimeAgenda(self):
        for item in self.__agenda:
            item.printAll() 

    def imprimePessoa(self, index :int):
        pes = self.__agenda[index]
        pes.printAll()


if __name__ == '__main__':
    agenda = Agenda()
    print("Armazenando")
    agenda.armazenaPessoa("Tiago DAgostino", 39, 2.0)
    agenda.armazenaPessoa("Luciana Oguma", 37, 1.55)
    print("Imprimindo Tudo")
    agenda.imprimeAgenda()   
    print("Buscando")
    print(agenda.buscaPessoa("Tiago"))
    print(agenda.buscaPessoa("Tiago DAgostino"))    
    print("Imprimindo Busca")
    agenda.imprimePessoa(agenda.buscaPessoa("Tiago DAgostino"))
    print("Removendo Tiago")
    agenda.removePessoa("Tiago DAgostino")
    agenda.imprimeAgenda()   
    