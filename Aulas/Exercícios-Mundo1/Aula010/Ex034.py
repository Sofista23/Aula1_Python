sal=int(input("Digite o valor do seu salário:"))
if sal<=1250:
    porc=(sal*15)/100
    soma=porc+sal
    print("Seu novo salário é R${0}, com um aumento de 15%.".format(soma))
else:
    porc=(sal*10)/100
    soma=porc+sal
    print("Seu novo salário é R${0}, com um aumento de 10%.".format(soma))