t=0
r=0
while True:
    print("----------------------------------------------------------------")
    t=int(input("Digite um número (número negativo para o programa): "))
    print("----------------------------------------------------------------")
    if t>=0:
        for c in range(0,11):
            r=t*c
            print(f"{t} x {c} = {r}")
    else:
        break
print("Fim do programa!")