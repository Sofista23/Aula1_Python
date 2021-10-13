n=int(input("Digite um número:"))
x=0
for c in range(0,11):
    x=n*c
    print("{0} x {1} = {2}".format(n,c,x))