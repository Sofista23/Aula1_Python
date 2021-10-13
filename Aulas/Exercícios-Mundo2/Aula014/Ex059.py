n1=int(input("Digite um número: "))
n2=int(input("Digite mais um número: "))
print("[1]Soma")
print("[2]Subtrai")
print("[3]Multiplica")
print("[4]Divide")
print("[5]Finaliza")
r=0
res=0
while r != 5:
    r=int(input("Qual é sua escolha?: "))
    if r==1:
        res=n1+n2
        print("A soma é {0}.".format(res))
    elif r==2:
        res=n1-n2
        print("A subtração é {0}.".format(res))
    elif r==3:
        res=n1*n2
        print("A multiplicação é {0}.".format(res))
    elif r==4:
        res=n1/n2
        print("A divisão é {0}.".format(res))
print("Fim do programa.")