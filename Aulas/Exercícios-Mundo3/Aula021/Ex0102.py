def fat(x,s=0):
    f=1
    for c in range(x,0,-1):
        f*=c    
        if s==True:
            print(f"{f} x {c} = {f}") 
    return f

n=int(input("Digite um número:"))
m=int(input("Mostrar desenvolvimento [0=não/1=sim]:"))

r1=fat(n,m)

print(f"O fatorial de {n} é {r1}.")