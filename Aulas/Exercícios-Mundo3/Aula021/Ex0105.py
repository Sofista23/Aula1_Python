def notas(*nota):
    lista={}
    s=0

    print(f"Foram digitadas {len(nota)} nota(s).")

    for c in range(0,len(nota)):
        s+=nota[c]
    media=s/len(nota)
    lista["média"]=media
    print(f"A média das notas é {lista['média']}.")

    lista["maior"]=max(nota)
    print(f"A maior nota é {lista['maior']}.")

    lista["menor"]=min(nota)
    print(f"A menor nota é { lista['menor']}.")

    if media>7:
        lista["res"]="Aprovado"
    elif media>5:
        lista["res"]="Recuperação"
    else:
        lista["res"]="Reprovado"
    print(f"Situação: {lista['res']}")

    print(lista)

notas(4,8,6,4)
print("-="*35)
notas(5,4,6,7,5)