def par(num):
    if num%2==0:
        return True
    else:
        return False

n=int(input("Digite um número:"))
if par(n)==True:
    print(f"{n} é Par!")
else:
    print(f"{n} é Ímpar!")