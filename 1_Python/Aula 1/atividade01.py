import random

f = open(r"./LISTA_PESSOAS PARA SORTEIO.txt", "r")
pessoas = []
for line in f:
    #print(line)
    pessoas.append(line)
f.close()

s = open(r"./resultado.txt", "w+")
for n in range(3):
    sorteio = random.randrange(1, len(pessoas), 1)
    #print(sorteio)
    pessoa = pessoas.pop(sorteio)
    print(pessoa)
    s.write(pessoa)

s.close()