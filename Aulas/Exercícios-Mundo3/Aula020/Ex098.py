def cont(ini,fim,pas):
    for c in range(ini,fim,pas):
        print(c)

cont(1,11,1)

print("-="*30)

cont(10,0,-2)

print("-="*30)

i=int(input("Digite o início da Contagem:"))
f=int(input("Digite o fim da Contagem:"))
print("Passo negativo faz contagem regressiva!")
p=int(input("Digite o passo da Contagem:"))

cont(i,f,p)