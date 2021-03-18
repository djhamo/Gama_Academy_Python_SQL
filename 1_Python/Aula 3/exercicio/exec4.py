"""
4.	Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume e trocar os canais da televisão. 
O controle de volume permite:
a.	Aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
b.	Aumentar e diminuir o número do canal em uma unidade
c.	Trocar para um canal indicado;
d.	Consultar o valor do volume de som e o canal selecionado
"""
class Televisao(object):
    __volume = int()
    __volume_max = int()
    __canal = int()

    def __init__(self):
        self.__volume_max = 10;

    def getVolume(self):
        return self.__volume

    def getCanal(self):
        return self.__canal

    def aumentaVolume(self):
        if self.__volume + 1 <= self.__volume_max:
            self.__volume += 1   
        else:
            raise Exception("Volume Maximo") 

    def diminuiVolume(self):
        if self.__volume > 0 :
            self.__volume -= 1   
        else:
            raise Exception("Volume Minimo") 

    def aumentaCanal(self):
        self.__canal += 1

    def diminuiCanal(self):
        if self.__canal > 0 :
            self.__canal -= 1   
        else:
            raise Exception("Canal zero") 

class ControleRemoto(object):
    __tv = Televisao()

    def __init__(self, tv : Televisao):
        self.__tv = tv

    def getVolume(self):
        return self.__tv.getVolume()

    def getCanal(self):
        return self.__tv.getCanal()

    def aumentaVolume(self):
        self.__tv.aumentaVolume()

    def diminuiVolume(self):
        self.__tv.diminuiVolume()

    def aumentaCanal(self):
        self.__tv.aumentaCanal()

    def diminuiCanal(self):
        self.__tv.diminuiCanal()
 

if __name__ == '__main__':
    tv = Televisao()
    ctrl = ControleRemoto(tv)
    try:
        for i in range(15):
            print(f"Aumentando volume +1 .. {i}")
            print(ctrl.getVolume())
            ctrl.aumentaVolume()   
    except Exception as e:
        print(e)    

    try:
        for i in range(15):
            print(f"Diminuindo volume +1 .. {i}")
            print(ctrl.getVolume())
            ctrl.diminuiVolume()   
    except Exception as e:
        print(e)            

    try:
        for i in range(15):
            print(f"Aumentando Canal +1 .. {i}")
            print(ctrl.getCanal())
            ctrl.aumentaCanal()   
    except Exception as e:
        print(e)    

    try:
        for i in range(17):
            print(f"Diminuindo vcanal +1 .. {i}")
            print(ctrl.getCanal())
            ctrl.diminuiCanal()   
    except Exception as e:
        print(e)                    