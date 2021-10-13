val=[]
cont=0
while True:
    val.append(int(input("Digite um número:")))
    cont += 1
    esc=input("Continuar?[s/n]:").upper().strip()
    if esc=="N":
        break
print("="*50)
print(f"Foram digitados {cont} valor(s).")
print(sorted(val))
if 5 in val:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")
print(sorted(val,reverse=True))