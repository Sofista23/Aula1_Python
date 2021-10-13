n=0
s=0
q=0
while n != 999:
    n=int(input("Digite um número:"))
    if n != 999:
        s += n
        q += 1
print("A soma de todos os números é {0}.".format(s))
print("A quantidade de números digitados foi de {0}.".format(q))
