from random import randint
nums=[]
def sorteia(n):
    for c in range(0,5):
        a=randint(0,10)
        n.append(a) 
    print(f"O sorteio ficou: {n}")

def par(v):
    s=0
    for c in range(0,5):
        if v[c]%2==0:
            s+=v[c]
    print(f"A soma de todos os pares é {s}.")

sorteia(nums)
par(nums)

