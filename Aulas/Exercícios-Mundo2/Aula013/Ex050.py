s=0 
count=0
for c in range(1,7):
    n=int(input("Digite um número:"))
    if n%2==0:
        s += n
        count += 1
print("A soma dos {0} valores pares é {1}.".format(count,s))