import Moeda

n=float(input("Digite o valor restante em seu carrinho:"))

print(f"A soma de {Moeda.ajuste(n)} pela sua metade é {Moeda.ajuste(Moeda.aumentar(n))}")
print(f"A soma de {Moeda.ajuste(n)} pela sua metade é {Moeda.ajuste(Moeda.aumentar(n))}")
print(f"A subtração de {Moeda.ajuste(n)} pela sua metade é {Moeda.ajuste(Moeda.diminuir(n))}")
print(f"O dobro de {Moeda.ajuste(n)} é {Moeda.ajuste(Moeda.dobro(n))}")
print(f"A metade de {Moeda.ajuste(n)} é {Moeda.ajuste(Moeda.metade(n))}")