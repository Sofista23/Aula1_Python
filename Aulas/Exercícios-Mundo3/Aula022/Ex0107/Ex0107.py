import Moeda

n=float(input("Digite o valor restante em seu carrinho:"))

print(f"A soma de {n} pela sua metade é {Moeda.aumentar(n)}")
print(f"A subtração de {n} pela sua metade é {Moeda.diminuir(n)}")
print(f"O dobro de {n} é {Moeda.dobro(n)}")
print(f"A metade de {n} é {Moeda.metade(n)}")