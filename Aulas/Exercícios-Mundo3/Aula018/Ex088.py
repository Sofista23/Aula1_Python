from random import randint
from time import sleep
cont=0
lista=[]
jogos=[]
quant=int(input("Quantiade de vezes de palpites:"))
tot=0
while tot<=quant:
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(jogos)