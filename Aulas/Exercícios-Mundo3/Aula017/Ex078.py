val=[]
for c in range(0,5):
    if c==0:
        val.append(int(input("Digite um valor: ")))
    else:
        val.append(int(input("Digite mais um valor: ")))
print(f"Os valore digitados foram {val}")
max=max(val)
min=min(val)
for i,v in enumerate(val):
    if val[i]==max:
        print(f"O maior valor é o {max} e está na posição {i+1}.")
    if val[i]==min:
        print(f"O menor valor é o {min} e está na posição {i+1}.")