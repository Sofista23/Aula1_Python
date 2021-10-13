k=int(input("Digite a distância do seu destino:"))
if k<=200:
    mul=k*0.50
    print("Sua viagem vai custar R${0}.".format(mul))
else:
    mul=k*0.45
    print("Sua viagem vai custar R${0}.".format(mul))