n1=int(input("Digite um número:"))
n2=int(input("Digite outro um número:"))
n3=int(input("Digite mais um número:"))
if n1>n2 and n1>n3 and n2>n3:
    print("{0} é o maior número.".format(n1))
    print("{0} é o menor número.".format(n3))
if n1>n2 and n1>n3 and n2<n3:
    print("{0} é o maior número.".format(n1))
    print("{0} é o menor número.".format(n2)) 
if n2>n1 and n2>n3 and n1>n3:
    print("{0} é o maior número.".format(n2))
    print("{0} é o menor número.".format(n3)) 
if n2>n1 and n2>n3 and n1<n3:
    print("{0} é o maior número.".format(n2))
    print("{0} é o menor número.".format(n1)) 
if n3>n1 and n3>n2 and n1>n2:
    print("{0} é o maior número.".format(n3))
    print("{0} é o menor número.".format(n2)) 
if n3>n1 and n3>n2 and n1<n2:
    print("{0} é o maior número.".format(n3))
    print("{0} é o menor número.".format(n1)) 