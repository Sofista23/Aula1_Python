help(print)

def count(i,f,p):
    """ 
    Faz uma contagem na tela
    para i: Inicio da contagem
    para f: fim da contagem
    para p: passo da contagem
    return: sem retorno
    """
    for c in range(i,f,p):
        print(c)
    print("Fim")  
help(count)


def somar(a=0,b=0,c=0):
    s=a+b+b
    print(s)
#ou
def soma(*n):
    s=0
    for c in range(0,len(n)):
        s+=n[c]
    print(s)
somar(4,5,7)
soma(1,5,2,4,6,3)


def mult(a,b,c):        
    m=a*b*c
    return m
r1=mult(4,5,8)
r2=mult(2,5,7)
r3=mult(1,9,8)
print(f"As resposta são {r1}, {r2} e {r3}.")