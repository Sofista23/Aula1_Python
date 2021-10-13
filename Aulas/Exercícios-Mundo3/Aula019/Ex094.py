cad={}
lista=[]
qtn=0
fem=[]
qtnFem=0
idade=[]
qtnIdade=0
media=0
while True:
    cad["nome"]=input("Nome:")
    cad["sexo"]=input("Sexo[m/f]:").strip().upper()
    cad["idade"]=int(input("Idade:"))

    if cad["sexo"]=="F":
        fem.append(cad["nome"])
        qtnFem+=1

    if cad["idade"]>=21:
        idade.append(cad["nome"])
        qtnIdade+=1

    lista.append(cad.copy())

    qtn+=1

    media+=cad["idade"]

    esc=input("Continuar[s/n]:").upper().strip()
    if esc=="N":
        break

media2=media/len(cad)

print(lista)
print(f"Foram cadastradas {qtn} pessoas.")
print(f"Foram cadastradas {qtnFem} mulheres: {fem}")
print(f"Foram cadastradas {qtnIdade} pessoas maiore de 21 anos: {idade}")
print(f"A média das idades é {media2}.")