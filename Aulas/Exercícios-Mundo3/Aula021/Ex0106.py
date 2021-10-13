def manual():
    while True:
        x=input("Digite uma Função ou uma Biblioteca:")
        help(x)
        if x=="fim":
            break

manual()

print("Fim do Programa!")