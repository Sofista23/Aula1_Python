n=1
p=0
i=0
while n != 0:
    n=int(input("Digite um valor:"))
    if n%2==0:
        if n != 0:
            p += 1
    else:
        i += 1
print("A quantidade de números pares foi {0} e de números ímpares foi{1}.".format(p,i))
print("Fim.")