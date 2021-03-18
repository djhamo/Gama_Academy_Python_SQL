"""
3.	Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. 
   A classe deve armazenar o andar atual (térreo = 0), 
   total de andares no prédio (desconsiderando o térreo), 
   capacidade do elevador e quantas pessoas estão presentes nele. 
   A classe deve também disponibilizar os seguintes métodos:
a.	Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio 
(os elevadores sempre começam no térreo e vazio);
b.	Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
c.	Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
d.	Sobe: para subir um andar (não deve subir se já estiver no último andar);
e.	Desce: para descer um andar (não deve descer se já estiver no térreo);
"""

class Elevador(object):
    __andar_atual = int()
    __total_andares = int()
    __capacidade = int()
    __tot_pessoas = int()

    def __init__ (self, capacidade: int, tot_andares_predio: int):
        self.__andar_atual = 0
        self.__total_andares = tot_andares_predio
        self.__capacidade = capacidade
        self.__tot_pessoas = 0

    def entra(self):
        if self.__tot_pessoas + 1 <= self.__capacidade:
            self.__tot_pessoas += 1   
        else:
            raise Exception("Elevador lotado")    

    def sai(self):
        if self.__tot_pessoas > 0:
            self.__tot_pessoas -= 1 
        else:
            raise Exception("Elevador vazio")    

    def sobe(self):
        if self.__andar_atual + 1 <= self.__total_andares:
            self.__andar_atual += 1   
        else:
            raise Exception("Elevador no último andar")    

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1 
        else:
            raise Exception("Elevador no terreo")    

if __name__ == '__main__':
    elev = Elevador(10, 5)
    for i in range(11):
        print('Entra 1')
        try:
            elev.entra()
        except Exception as e:
            print(e)    

    for i in range(11):
        print('Sai 1')
        try:
            elev.sai()    
        except Exception as e:
            print(e)    

    for i in range(6):
        print('Sobe 1')
        try:
            elev.sobe()        
        except Exception as e:
            print(e)    

    for i in range(7):
        print('Desce 1')
        try:
            elev.desce()            
        except Exception as e:
            print(e)    
