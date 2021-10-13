def areaT(l,c):
    print(f"A área do triângulo com as dimenções {l} de largura e {c} de comprimento é {(l*c)/2}.")
def areaQ(l,c):
    print(f"A área do Retângulo com as dimenções {l} de largura e {c} de comprimento é {l*c}.")
def areaO(r):
    print(f"A área do Círculo com raio igual a {r} é {(r**2)*3.14}")

while True:

    esc=int(input("Área do Ttiângulo[0], do Retângulo[1] e do Círculo[2] (999 para):"))
    print("-="*40)
    if esc==0:
        larg=int(input("Digite o valor da largura:"))
        alt=int(input("Digite o valor da altura:"))
        areaT(larg,alt)
        print("-="*40)

    elif esc==1:
        larg=int(input("Digite o valor da largura:"))
        alt=int(input("Digite o valor da altura:"))
        areaQ(larg,alt)
        print("-="*40)

    elif esc==2:
        raio=int(input("Digite o valor do raio:"))
        print("Pi vai valer 3,14")
        areaO(raio)
        print("-="*40)
    
    elif esc==999:
        break
    
    else:
        print("Valor passado inválido. Tente novamente.")
        print("-="*40)

print("-="*40)
print("Finalizado!")