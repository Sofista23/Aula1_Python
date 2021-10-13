def fat(x=1):
    f=1
    for c in range(x,0,-1):
        f*=c
    return f

n=int(input("Digite um número:"))

r1=fat(n)

print(f"O fatorial de {n} é {r1}.")