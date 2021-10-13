print("Condição de existência de um TRIÂNGULO")
r1=int(input("Primeira reta:"))
r2=int(input("Segunda reta:"))
r3=int(input("Terceira reta:"))
if r1>r2-r3 and r1<r2+r3:
    print("Passou")
if r2>r1-r3 and r2<r1+r3:
    print("Passou")
if r3>r2-r1 and r3<r2+r1:
    print("Passou")
else:
    print("Impossível")