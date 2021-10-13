n=int(input("Digite um número:"))
tot=0
for c in range(1,n+1):
    if n%c==0:
        print("{0}\033[33m".format(c),end=" ")
        tot +=1
    else:
        print("{0}\033[31m".format(c),end=" ")
if tot==2:
    print("É primo.")
else:
    print("Não é primo.")