k=int(input("Digite a velocidade do seu carro:"))
if k<=80:
    print("Tudo certo, diriga com segurança.")
else:
    s=k-80
    m=s*7
    print("Você ultrapassou o limite de velocidade e terá que pagar uma multa de R${0}.".format(m))