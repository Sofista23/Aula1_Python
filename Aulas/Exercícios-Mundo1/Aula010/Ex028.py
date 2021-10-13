import random
n1=int(input("Digite um número de 0 a 5:"))
lista=[0,1,2,3,4,5]
x=random.choice(lista)
if n1==x:
    print("Você ganhou!!! Seu número é igual ao escolhido.")
else:
    print("Você perdeu!!! Seu número foi diferente do escolhido, que foi {0}.".format(x))