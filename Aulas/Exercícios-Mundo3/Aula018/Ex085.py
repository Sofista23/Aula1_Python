princ=[]
p=[]
i=[]
for c in range(1,8):
    esc=int(input(f"Digite o {c}° valor:"))
    if esc%2==0:
        p.append(esc)
    else:
        i.append(esc)
princ.append(p)
princ.append(i)
print("-="*45)
print(f"Pares: {sorted(princ[0])}")
print(f"Ímpares: {sorted(princ[1])}")
