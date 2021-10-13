p=[]
dados=[]
for c in range(0,2):
    dados.append(input("Nome:"))
    dados.append(int(input("Idade:")))
    p.append(dados[:])
    dados.clear()

for c in p:
    if c[1]>=18:
        print(f"{c[0]} é maior de idade.")
    else:
        print(f"{c[0]} é menor de idade.")

print(p)