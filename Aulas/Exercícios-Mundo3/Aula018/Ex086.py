matriz=[]
l1=[]
l2=[]
l3=[]
for c in range(1,10):
    nums=int(input(f"Digite o {c}° valor:"))
    if c<=3:
        l1.append(nums)
    elif c<=6:
        l2.append(nums)
    else:
        l3.append(nums)
matriz.append(l1)
matriz.append(l2)
matriz.append(l3)
print("-="*45)
print("Matriz 3x3:")
print(matriz[0])
print(matriz[1])
print(matriz[2])