ficha=[]
for c in range(0,2):
    n=input("Nome:")
    n1=int(input("Nota 1:"))
    n2=int(input("Nota 2:"))
    media=(n1+n2)/2
    ficha.append([n,[n1,n2],media])
for i in ficha:
    print(f"Nome: {i[0]} -> Média= {i[2]}")