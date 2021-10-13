import random
n1=int(input("Digite um número de 0 a 5:"))
lista=[0,1,2,3,4,5]
x=random.choice(lista)
while n1 != x:
    n1=int(input("Errouuu! Tente outra vez!!! Digite um número de 0 a 5:"))
print("Acertou!")