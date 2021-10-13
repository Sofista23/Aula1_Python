print("Preço Total = R$1200")
fpag=int(input("Como vai pagar? [1]Cartão [2]Cheque/Dinheiro:"))
if fpag==1:
    pres=int(input("Em quantas vezes vai ser o pagamento?:"))
    if pres==1:
        x=(1200*5)/100
        total=1200-x
        print("Pagamento no cartão á vista, com 5'%' de desconto.")
        print("Total á pagar = R${0}".format(total))
    elif pres==2:
        print("Pagamento no cartão em 2x, sem desconto.")
        print("Total á pagar = 2x de R$600")
    elif pres>=3:
        x=(1200*20)/100
        total=1200+x
        print("Pagamento no cartão em 3x ou mais, com 20'%' de juros")
        print("Total á pagar = {0}".format(total))
else:
    x=(1200*10)/100
    total=1200-x
    print("Pagamento á vista no cheque/dinheiro, com 10'%' de desconto.")
    print("Total á pagar = {0}".format(total))