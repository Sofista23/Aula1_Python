soma=0
idm=0
hmv=0
hnmv=""
for c in range(1,4):
    print("----- {0}° Pessoa -----".format(c))
    n=input("Nome: ")
    i=int(input("Idade: "))
    s=input("Sexo [M/F]:")
    soma += i
    if s=="F" or s=="f":
        if i<18:
            idm += 1
    if c==1 and s=="M" and s=="m":
        hmv=n
        hnmv=n
    if s=="M" and s=="m"and i>hmv:
        hmv=i
        hnmv=n
media=soma/c
print("A média de todas as idades é {0}.".format(media))
print("Tem ao todo {0} mulhere(s) menores de idade.".format(idm))
print("O homem mais velho é o {0} e tem {1} ano(s).".format(hnmv,hmv))