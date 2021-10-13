id=int(input("Digite sua idade:"))
if id<9:
    print("Com a idade de {0} você é um nadador MIRIM.".format(id))
elif id>=9 and id<14:
    print("Com a idade de {0} você é um nadador INFANTIL.".format(id))
elif id>=14 and id<19:
    print("Com a idade de {0} você é um nadador JUNIOR.".format(id))
elif id>=19 and id<25:
    print("Com a idade de {0} você é um nadador SÊNIOR.".format(id))
else:
    print("Com a idade de {0} você é um nadador MASTER.".format(id))