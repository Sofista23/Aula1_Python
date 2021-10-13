n1=int(input("Digite um valor:"))
n2=int(input("Digite mais um valor:"))
if n1>n2:
    print("{0} maior que {1}.".format(n1,n2))
elif n2>n1:
    print("{0} maior que {1}.".format(n2,n1))
else:
    print("Os valores são iguais.")