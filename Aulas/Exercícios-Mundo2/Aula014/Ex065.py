n=0
s=0
q=0
ma=0
me=0
while n != 666:
    n=int(input("Digite um número:"))

    if n != 666:
        s += n
        q += 1

    if n != 666:
        if q==1:
            ma=me=n
        else:
            if n>ma:
                ma=n
            if n<me:
                me=n
m=s/q
print("A média dos números digitados foi de {0}.".format(m))
print("O maior número foi {0} e o menor foi {1}.".format(ma,me))
print("Fim!")