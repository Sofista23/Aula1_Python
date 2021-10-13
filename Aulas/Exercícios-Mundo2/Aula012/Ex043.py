peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
imc=peso/(altura**2)
if imc<18.5:
    print("Índice de Massa Corpórea = {0}".format(imc))
    print("Abaixo do peso.")
elif imc>=18.5 and imc<25:
    print("Índice de Massa Corpórea = {0}".format(imc))
    print("Peso ideal.")
elif imc>=25 and imc<30:
    print("Índice de Massa Corpórea = {0}".format(imc))
    print("Sobrepeso.")
elif imc>=30 and imc<40:
    print("Índice de Massa Corpórea = {0}".format(imc))
    print("Obesidade.")
else:
    print("Índice de Massa Corpórea = {0}".format(imc))
    print("Obesidade móbida.")