n=(int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")))
print(f"Você digitou os númros {n}.")
if 9 in n:
    print(f"O valor nove apareceu {n.count(9)} vezes.")
if 3 in n:
    print(f"O valor 3 apareceu na {n.index(3)+1}° posição pela primeira vez.")
for c in n:
    if c%2==0:
        print(f"{c} é um valor par.")
print("Fim do programa.")