val=[]
par=[]
impar=[]
while True:
    v=int(input("Digite um número:"))
    val.append(v)
    if v%2==0:
        par.append(v)
    else:
        impar.append(v)
    esc=input("Continua?[s/n]:").strip().upper()
    if esc=="N":
        break
print(f"A lista completa é {val}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")
