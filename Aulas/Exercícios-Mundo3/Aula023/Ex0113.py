def leiaInt():
    while True:
        try:
            val=int(input("Digite um número inteiro:"))
        except:
            print("Erro!")
            continue
        else:
            return val

def leiafloat():
    while True:
        try:
            val=float(input("Digite um número float:"))
        except:
            print("Erro!")
            continue
        else:
            return val


ri=leiaInt()
rf=leiafloat()

print(f"Você digitou o valor inteiro {ri}.")
print(f"Você digitou o valor float {rf}.")
