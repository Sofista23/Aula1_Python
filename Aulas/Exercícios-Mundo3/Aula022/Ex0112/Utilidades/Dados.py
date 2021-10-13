def leia(msg):
    valido=False
    while not valido:
        entrada=input(msg)
        if entrada.isalpha():
            print("Preço inválido")
        else:
            valido=True
            return float(entrada)