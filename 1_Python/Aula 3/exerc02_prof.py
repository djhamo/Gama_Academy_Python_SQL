"""
2.	Crie uma classe Agenda que pode armazenar 10 pessoas e que seja capaz de realizar as seguintes operações:
    a.	armazenaPessoa(String nome, int idade, float altura)
    b.	removePessoa(String nome)
    c.	buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
    d.	imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
    e.	imprimePessoa(int index); // imprime os dados da pessoa que está na posição “i” da agenda.
"""

class Agenda(object):
    listPessoas = []

    def armazenaPessoa(self, nome, idade, altura):
        if len(self.listPessoas) < 10:
            dic = {}
            dic["nome"] = nome
            dic["idade"] = idade
            dic["altura"] = altura
            self.listPessoas.append(dic)
        else:
            print("Agenda cheia. Não é possível mais inserir novas pessoas...")

    def removePessoa(self, nome):
        if len(self.listPessoas) == 0:
            print("Lista vazia. Insira pessoas primeiro...")
        else:
            for pessoa in self.listPessoas:
                if pessoa["nome"] == nome:
                    self.listPessoas.remove(pessoa)
                    return

            print("Pessoa não encontrada...")

    def buscaPessoa(self, nome):
        for pessoa in self.listPessoas:
            if pessoa["nome"] == nome:
                return self.listPessoas.index(pessoa)

        return -1

    def imprimeAgenda(self):
        for pessoa in self.listPessoas:
            print(pessoa)

    def imprimePessoa(self, index):
        print(self.listPessoas[index])

def recebeOpcaoUsuario():
    opcao = 0

    print("Digite a opção que deseja executar:\n"
          "1 - Armazena Pessoa na Agenda\n"
          "2 - Remove Pessoa\n"
          "3 - Imprimir Pessoa pelo nome\n"
          "4 - Imprimir Agenda\n"
          "5 - Imprimir Pessoa pelo índice\n"
          "6 - Sair do Programa\n")

    while opcao < 1 or opcao > 6:
        opcao = int(input("Digite uma opção válida (1 - 6): "))
        if opcao < 1 or opcao > 6:
            print("Opção inválida. Digite novamente")

    return opcao

if __name__ == '__main__':
    opcao = recebeOpcaoUsuario()
    agenda = Agenda()

    while opcao >= 1 and opcao <= 6:
        if opcao == 1: #Armazenamento de Pessoa
            print("Opção 1 - Armazenamento de Pessoa\n")
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            altura = float(input("Digite a altura: "))

            agenda.armazenaPessoa(nome, idade, altura)
        elif opcao == 2: #Remover Pessoa
            print("Opção 2 - Remoção de Pessoa")
            nome = input("Digite o nome: ")

            agenda.removePessoa(nome)
        elif opcao == 3: #Imprimir pessoa por nome
            print("Opção 3 - Busca de Pessoa pelo nome")
            nome = input("Digite o nome: ")

            print(agenda.buscaPessoa(nome))
        elif opcao == 4: #imprimir a Agenda
            print("Opção 4 - Imprimir Agenda Completa")
            agenda.imprimeAgenda()
        elif opcao == 5: #imprimir pessoa por índice
            print("Opção 5 - Imprimir Pessoa por índice")
            indice = int(input("Digite o índice: "))

            agenda.imprimePessoa(indice)
        else: #sair do programa
            print("Você saiu do programa. Obrigado por usar...\n")
            opcao = 7

        if opcao != 7:
            opcao = recebeOpcaoUsuario()
