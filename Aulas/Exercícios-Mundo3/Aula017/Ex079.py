val=[]
while True:
    n=int(input("Digite um valor:"))
    if n not in val:
        val.append(n)
    else:
        print("Valor digitado anteriormente.")
    esc=input("Continua?[s/n]:").upper().strip()
    if esc=="N":
        break
print(f"Você digitou os valores {sorted(val)}")