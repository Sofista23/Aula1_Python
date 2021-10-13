matriz=[]
l1=[]
l2=[]
l3=[]
p=0
for c in range(1,10):
    nums=int(input(f"Digite o {c}° valor:"))

    if c<=3:
        l1.append(nums)
    elif c<=6:
        l2.append(nums)
    else:
        l3.append(nums)

    if nums%2==0:
        p+=nums
    
matriz.append(l1)
matriz.append(l2)
matriz.append(l3)

print("-="*45)

print("Matriz 3x3:")
print(matriz[0])
print(matriz[1])
print(matriz[2])

print("-="*45)

print(f"A soma de todos os valores pares é {p}.")

st=matriz[0][2]+matriz[1][2]+matriz[2][2]
print(f"A soma de todos os valores da terceira coluna é {st}.")

maior=max(l2)
print(f"O maior valor da 2° linha é o {maior}.")