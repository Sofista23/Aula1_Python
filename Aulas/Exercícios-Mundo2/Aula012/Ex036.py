emp=int(input("Digite o valor do empréstimo:"))
pres=int(input("Digite a quantidade de prestações:"))
sal=int(input("Digite o valor do seu salário:"))
calc1=(sal*30)/100
calc2=emp/pres
if(calc1<=calc2):
    print("Empréstimo pode ser realizado.")
else:
    print("Emprétimo não pode ser realizado.")