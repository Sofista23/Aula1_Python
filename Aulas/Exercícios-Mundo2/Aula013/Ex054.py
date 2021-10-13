ma=0
me=0
for c in range(1,6):
    dt=int(input("Em que ano a {0}° pessoa nasceu? ".format(c)))
    x=2021-dt
    if x<18:
        me += 1
    else:
        ma += 1
print("Ao todo tivemos {0} pessoa(s) menores de idade.".format(me))
print("Ao todo tivemos {0} pessoa(s) mmaiores de idade.".format(ma))