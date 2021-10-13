t=("Computador",4000,"Celular",2500,"CPU",900)
print("-"*30)
print("Listagem de Preços")
print("-"*30)
for c in range(0,len(t)):
    if c%2==0:
        print(t[c],"."*30,end="")
    else:
        print(f"R${t[c]}")