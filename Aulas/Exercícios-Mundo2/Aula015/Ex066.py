n=0
s=0
c=0
while True:
    n=int(input("Digite um número (999 para o programa): "))
    if n != 999:
        s += n
        c += 1
    else:
        break
print(f"A soma do(s) {c} número(s) digitado(s) foi {s}.")
