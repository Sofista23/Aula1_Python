princ=[]
dados=[]
mais=[]
menos=[]
quant=0
while True:
    dados.append(input("Nome:"))
    dados.append(int(input("Peso:")))
    princ.append(dados[:])
    quant+=1
    dados.clear()
    esc=input("Continuar?[s/n]:").strip().upper()
    if esc=="N":
        break
for v in princ:
    if v[1]>=95:
        mais.append(v[0])
    else:
        menos.append(v[0])
print(princ)
print(f"Foram cadastradas {quant} pessoa(s).")
print(f"Mais pesados: {mais}")
print(f"Mais leves: {menos}")