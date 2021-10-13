from random import randint
comp=randint(0,10)
poui=0
esc=0
soma=0
vit=0
while True:
    poui=int(input("Par[1] Ímpar[2]: "))
    esc=int(input("Digite um número de 1 a 10 (seguindo sua escolha anterior): "))
    soma=esc+comp
    if poui==1:
        if soma%2==0:
            print("Você gangou!")
            vit += 1
        else:
            print("Você perdeu!")
            break
    elif poui==2:
        if soma%2==0:
            print("Você perdeu!")
            break
        else:
            print("Você ganhou!")
            vit += 1
    else:
        print("Dados fornecidos inválidos!")
        break
print(f"Você ganhou {vit} seguida(s).")
print("Game Over!")