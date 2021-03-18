#Programação Orientada a Objetos em Python

#Classe Publica: apenas o nome
#Classe Protected: 1 underline na frente no nome (_)
#Classe Private: 2 underline na frente no nome(__)

from classes.cadastros import seguranca as seg

objUsuario = seg.Usuario()
objPerfilAcesso = seg.PerfilAcesso()

class Carro(object):
    marca = "Fiat"
    modelo = "Uno de firma"

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligarMotor(self):
        return 0


class Cliente(object):
    pass

objCliente = Cliente()
objCliente.nome = ""
objCliente.dtNasc = ""

if __name__ == '__main__':
    pass
