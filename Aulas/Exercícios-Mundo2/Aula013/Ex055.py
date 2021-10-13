ma=0
me=0
for c in range(1,5):
    p=float(input("Peso da {0}° pessoa:".format(c)))
    if c==1:
        ma=p
        me=p
    else:
        if p>ma:
            ma=p
        if p<me:
            me=p
print("O maior peso foi de {0}Kg.".format(ma))
print("O menor peso foi de {0}Kg.".format(me))