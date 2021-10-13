n=""
p=0
total=0
pcaros=0
cont=""
menor=0
nmenor=""
print("--------------------")
print("Carrinho de Compras")
print("--------------------")
while True:
    n=input("Nome do produto: ")
    p=int(input("Preço do produto: "))
    total += p
    if p>1000:
        pcaros += 1
    if cont==1:
        menor=p
        nmenor=n
    else:
        if p<menor:
            menor=p
            nmenor=n
    cont=input("Continuar Comprando [s/n]? ").upper().strip()
    if cont=="N":
        break
print(f"Total: {total}")
print(f"Produtos com preço superior a R$1000: {pcaros}")
print(f"O produto {nmenor} é o mais barato e custa R${menor}.")
print("Pedido Fechado!")